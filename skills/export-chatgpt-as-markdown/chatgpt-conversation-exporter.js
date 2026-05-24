#!/usr/bin/env node
/**
 * ChatGPT Conversation Exporter — Skill
 * ======================================
 * Exports a ChatGPT conversation page to Markdown.
 * Downloads all AI-generated images and embeds local links in the .md file.
 *
 * Usage: Run this script in the browser DevTools console while on a
 *        ChatGPT conversation page (chatgpt.com/c/...).
 *
 * Output:
 *   - <conversation-title>.md      — Full conversation in Markdown
 *   - image-NN-<slug>.png          — All AI-generated images (downloaded separately)
 *
 * The .md file uses local relative paths for all images so that placing
 * the .md and all .png files in the same folder renders correctly.
 */

// ─────────────────────────────────────────────
// 1. UTILITY FUNCTIONS
// ─────────────────────────────────────────────

/** Convert a DOM node tree to Markdown text */
function nodeToMarkdown(node) {
  if (node.nodeType === 3) return node.textContent;
  if (node.nodeType !== 1) return '';

  const tag = node.tagName.toLowerCase();
  const children = Array.from(node.childNodes).map(c => nodeToMarkdown(c)).join('');

  switch (tag) {
    case 'h1': return `\n# ${children.trim()}\n`;
    case 'h2': return `\n## ${children.trim()}\n`;
    case 'h3': return `\n### ${children.trim()}\n`;
    case 'h4': return `\n#### ${children.trim()}\n`;
    case 'h5': return `\n##### ${children.trim()}\n`;
    case 'h6': return `\n###### ${children.trim()}\n`;
    case 'p':  return `\n${children.trim()}\n`;
    case 'br': return '\n';
    case 'strong': case 'b': return `**${children}**`;
    case 'em':    case 'i': return `*${children}*`;
    case 'code':
      return node.parentElement?.tagName === 'PRE'
        ? children
        : `\`${children}\``;
    case 'pre':        return `\n\`\`\`\n${children.trim()}\n\`\`\`\n`;
    case 'ul':         return `\n${children}\n`;
    case 'ol': {
      let idx = 0;
      return '\n' + Array.from(node.children)
        .map(li => `${++idx}. ${li.textContent.trim()}`)
        .join('\n') + '\n';
    }
    case 'li':         return `- ${children.trim()}\n`;
    case 'a':          return `[${children}](${node.getAttribute('href') || ''})`;
    case 'img': {
      const alt = node.getAttribute('alt') || '';
      if (alt.startsWith('Generated image:') && window._filenameMap?.[alt]) {
        return `\n![${alt}](${window._filenameMap[alt]})\n`;
      }
      return '';
    }
    case 'blockquote': return `\n> ${children.trim()}\n`;
    case 'hr':         return `\n---\n`;
    case 'table':      return `\n${children}\n`;
    case 'tr':         return `${children}|\n`;
    case 'th': case 'td': return `| ${children.trim()} `;
    case 'script': case 'style': case 'button': case 'svg': return '';
    default:           return children;
  }
}

/** Slugify a string for use as a filename */
function slugify(text) {
  return text
    .toLowerCase()
    .replace(/generated image:\s*/i, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** Fetch an image element's src and return a base64 data URL */
async function imageElementToDataUrl(imgElement) {
  const response = await fetch(imgElement.src);
  const blob = await response.blob();
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload  = () => resolve({ dataUrl: reader.result, mimeType: blob.type, size: blob.size });
    reader.onerror = reject;
    reader.readAsDataURL(blob);
  });
}

/** Trigger a browser download of a data URL as a named file */
function downloadDataUrl(dataUrl, filename) {
  const a = document.createElement('a');
  a.href     = dataUrl;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

/** Trigger a browser download of a text string as a named file */
function downloadText(text, filename, mimeType = 'text/markdown;charset=utf-8') {
  const blob = new Blob([text], { type: mimeType });
  const url  = URL.createObjectURL(blob);
  downloadDataUrl(url, filename);
  setTimeout(() => URL.revokeObjectURL(url), 5000);
}

// ─────────────────────────────────────────────
// 2. DISCOVER ALL GENERATED IMAGES
// ─────────────────────────────────────────────

async function collectGeneratedImages() {
  const allImgs  = document.querySelectorAll('img');
  const seenSrc  = new Set();
  const images   = [];

  allImgs.forEach(img => {
    if (
      img.alt &&
      img.alt.startsWith('Generated image:') &&
      img.src &&
      !seenSrc.has(img.src)
    ) {
      seenSrc.add(img.src);
      images.push(img);
    }
  });

  console.log(`[Exporter] Found ${images.length} unique generated image(s).`);

  const results = [];
  for (let i = 0; i < images.length; i++) {
    const img      = images[i];
    const filename = `image-${String(i + 1).padStart(2, '0')}-${slugify(img.alt)}.png`;
    console.log(`[Exporter] Downloading image ${i + 1}/${images.length}: ${filename}`);
    try {
      const { dataUrl, mimeType, size } = await imageElementToDataUrl(img);
      results.push({ alt: img.alt, filename, dataUrl, mimeType, size });
      downloadDataUrl(dataUrl, filename);
    } catch (err) {
      console.warn(`[Exporter] Failed to download "${img.alt}": ${err.message}`);
      results.push({ alt: img.alt, filename, error: err.message });
    }
  }

  return results;
}

// ─────────────────────────────────────────────
// 3. EXTRACT CONVERSATION TO MARKDOWN
// ─────────────────────────────────────────────

function buildMarkdown(filenameMap) {
  // Expose map on window so nodeToMarkdown img handler can access it
  window._filenameMap = filenameMap;

  const turns = document.querySelectorAll('[data-testid^="conversation-turn-"]');
  let md = [
    `# ${document.title}`,
    '',
    `**URL:** ${window.location.href}`,
    '',
    `**Exported:** ${new Date().toISOString()}`,
    '',
    '---',
    '',
  ].join('\n');

  turns.forEach(turn => {
    const h4    = turn.querySelector('h4')?.textContent?.trim();
    const isUser = h4 === 'You said:';
    const role   = isUser ? '**You:**' : '**ChatGPT:**';

    let content = '';

    if (isUser) {
      const textMsg = turn.querySelector('.text-message');
      content = textMsg ? textMsg.textContent.trim() : '';
    } else {
      // Collect images unique to this turn
      const seenImgs = new Set();
      const imgLines = [];
      turn.querySelectorAll('img').forEach(img => {
        const alt = img.getAttribute('alt') || '';
        if (alt.startsWith('Generated image:') && filenameMap[alt] && !seenImgs.has(alt)) {
          seenImgs.add(alt);
          imgLines.push(`![${alt}](${filenameMap[alt]})`);
        }
      });

      const markdownDiv = turn.querySelector('.markdown');
      if (markdownDiv) {
        content = nodeToMarkdown(markdownDiv).trim();
      } else {
        // Fallback: deduplicated paragraphs
        const seen = new Set();
        turn.querySelectorAll('p').forEach(p => {
          const txt = p.textContent.trim();
          if (txt && !seen.has(txt)) { seen.add(txt); content += txt + '\n'; }
        });
        content = content.trim();
      }

      // Append any image references not already embedded via nodeToMarkdown
      if (imgLines.length > 0) {
        const imgSection = '\n\n' + imgLines.join('\n') + '\n';
        if (!content.includes(imgLines[0])) content += imgSection;
      }
    }

    if (content) {
      md += `${role}\n\n${content}\n\n---\n\n`;
    }
  });

  delete window._filenameMap;
  return md;
}

// ─────────────────────────────────────────────
// 4. MAIN — run everything
// ─────────────────────────────────────────────

(async function main() {
  console.log('[Exporter] Starting ChatGPT conversation export…');

  // Step 1: Download all generated images
  const imageResults = await collectGeneratedImages();

  // Step 2: Build filename map  alt → filename
  const filenameMap = {};
  imageResults.forEach(r => { if (!r.error) filenameMap[r.alt] = r.filename; });

  // Step 3: Build markdown
  const md = buildMarkdown(filenameMap);
  console.log(`[Exporter] Markdown built: ${md.length} chars.`);

  // Step 4: Download markdown file
  const mdFilename = document.title
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '') + '.md';

  downloadText(md, mdFilename);
  console.log(`[Exporter] Done. Files saved:\n  ${mdFilename}\n${imageResults.map(r => '  ' + r.filename).join('\n')}`);
})();
