/**
 * Capture approved public pages as text snapshots.
 *
 * Several participating organisations publish through client-rendered sites.
 * A plain HTTP fetch of the-gathering.earth returns two visible words against
 * 320 KB of markup; rendered, the same page yields over a thousand. So the
 * corpus is built from rendered snapshots rather than live fetches.
 *
 * This runs outside the tested pipeline on purpose. Rendering is not
 * deterministic and pulls a browser; the ingest path must stay reproducible.
 * Capture writes a snapshot plus a manifest entry, and the loader reads only
 * the snapshot. The manifest carries the content hash, which is what makes the
 * weekly re-capture able to tell "changed" from "unchanged" without guessing.
 *
 * Usage, on a host with Playwright and a Chromium build available:
 *   node scripts/capture-snapshots.mjs [--config <path>] [--out <dir>]
 */

import { createHash } from "node:crypto";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import process from "node:process";

const DEFAULT_CONFIG = "proposal/hackathon-1/execution/snapshots/sources.json";
const DEFAULT_OUT = "proposal/hackathon-1/execution/snapshots";
const SETTLE_MS = 2500;
const NAV_TIMEOUT_MS = 45000;

function arg(flag, fallback) {
  const index = process.argv.indexOf(flag);
  return index === -1 ? fallback : process.argv[index + 1];
}

function sha256(text) {
  return createHash("sha256").update(text, "utf8").digest("hex");
}

/** Resolve a Chromium executable, tolerating a Playwright build mismatch. */
async function resolveBrowser(chromium) {
  const { readdir } = await import("node:fs/promises");
  const cacheRoot = path.join(process.env.HOME ?? "", ".cache", "ms-playwright");
  try {
    const entries = await readdir(cacheRoot);
    const shells = entries
      .filter((name) => name.startsWith("chromium_headless_shell-"))
      .sort();
    if (shells.length > 0) {
      const candidate = path.join(
        cacheRoot,
        shells[shells.length - 1],
        "chrome-headless-shell-linux64",
        "chrome-headless-shell",
      );
      return chromium.launch({ executablePath: candidate });
    }
  } catch {
    // No cache directory; fall through to Playwright's own resolution.
  }
  return chromium.launch();
}



/**
 * Import Playwright, tolerating the fact that it is not installed beside this
 * script. Node resolves ESM imports relative to the importing file, so running
 * from another checkout fails even when Playwright exists on the host.
 *
 * Override the search location with ARK_NODE_MODULES if it lives elsewhere.
 */
async function loadPlaywright() {
  try {
    return await import("playwright");
  } catch {
    const roots = [
      process.env.ARK_NODE_MODULES,
      path.join(process.env.HOME ?? "", ".hermes", "hermes-agent", "node_modules"),
      path.join(process.cwd(), "node_modules"),
    ].filter(Boolean);

    for (const root of roots) {
      const entry = path.join(root, "playwright", "index.js");
      try {
        return await import(pathToFileURL(entry).href);
      } catch {
        // try the next candidate
      }
    }
    throw new Error(
      `playwright not found. Searched: ${roots.join(", ")}. ` +
        "Set ARK_NODE_MODULES to the directory containing it.",
    );
  }
}

const NAV_MAX_WORDS = 3;
const NAV_MIN_RUN = 4;

/**
 * Remove runs of consecutive very short lines, which is what a rendered
 * navigation menu looks like as text. Isolated short lines are kept, because
 * those are usually headings.
 */
function stripNavigationRuns(lines) {
  const out = [];
  let run = [];

  const flush = () => {
    if (run.length > 0 && run.length < NAV_MIN_RUN) out.push(...run);
    run = [];
  };

  for (const line of lines) {
    const words = line.split(/\s+/).filter(Boolean).length;
    if (words > 0 && words <= NAV_MAX_WORDS) {
      run.push(line);
    } else {
      flush();
      out.push(line);
    }
  }
  flush();
  return out;
}

async function main() {
  const configPath = arg("--config", DEFAULT_CONFIG);
  const outRoot = arg("--out", DEFAULT_OUT);

  const config = JSON.parse(await readFile(configPath, "utf8"));
  const { chromium } = await loadPlaywright();
  const browser = await resolveBrowser(chromium);

  const manifest = [];
  let failures = 0;

  for (const org of config.organisations) {
    await mkdir(path.join(outRoot, org.organisation_id), { recursive: true });

    for (const source of org.sources) {
      const target = path.join(outRoot, org.organisation_id, `${source.slug}.md`);
      try {
        const page = await browser.newPage();
        await page.goto(source.url, {
          waitUntil: "networkidle",
          timeout: NAV_TIMEOUT_MS,
        });
        await page.waitForTimeout(SETTLE_MS);
        const rendered = await page.evaluate(() => document.body.innerText);
        await page.close();

        // Drop navigation chrome. Roughly half the lines on these sites are
        // menu items, and they crowd real prose out of the retrieved window:
        // a question about an organisation's mission came back with its nav
        // bar and the model honestly refused to answer.
        //
        // The signature of a menu is a *run* of very short lines. An isolated
        // short line is usually a heading and is kept, so this removes chrome
        // without removing structure.
        const cleaned = stripNavigationRuns(
          rendered.split("\n").map((line) => line.replace(/[ \t]+/g, " ").trim()),
        );

        const text = cleaned
          .join("\n")
          .replace(/\n{3,}/g, "\n\n")
          // Contact addresses are stripped at capture time. The repository is
          // public and CC0, so a committed address becomes a scrape target.
          // The agent never needs one to answer a question about an
          // organisation, and the canonical URL is retained either way.
          .replace(/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g, "[contact address removed]")
          .trim();

        // Named third parties are replaced with a role label. They appear in
        // testimonials and credits on the source pages, having consented to
        // their own organisation's site rather than to this corpus. The list
        // is explicit in the config, never inferred, so every redaction is
        // auditable and a re-capture cannot silently reintroduce a name.
        const redacted = (config.redact_names ?? []).reduce(
          (acc, name) => acc.split(name).join("[name removed]"),
          text,
        );

        const words = redacted.split(/\s+/).filter(Boolean).length;
        await writeFile(target, `# ${source.title}\n\n${redacted}\n`, "utf8");

        manifest.push({
          organisation_id: org.organisation_id,
          source_id: source.source_id,
          source_url: source.url,
          snapshot_path: path.relative(process.cwd(), target),
          captured_at: config.captured_at,
          content_sha256: sha256(redacted),
          rendered_words: words,
        });

        console.log(`ok    ${source.source_id}  ${words} words  -> ${target}`);
      } catch (error) {
        failures += 1;
        console.log(`FAIL  ${source.source_id}  ${error.message.split("\n")[0]}`);
      }
    }
  }

  await browser.close();

  const manifestPath = path.join(outRoot, "manifest.json");
  await writeFile(
    manifestPath,
    `${JSON.stringify({ captured_at: config.captured_at, snapshots: manifest }, null, 2)}\n`,
    "utf8",
  );

  console.log(`\n${manifest.length} captured, ${failures} failed`);
  console.log(`manifest: ${manifestPath}`);
  process.exit(failures > 0 && manifest.length === 0 ? 1 : 0);
}

main();
