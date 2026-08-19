---
organisation_id: bad-permission
display_name: Valid Organisation
profile: A public interest organisation working on soil restoration.
themes:
  - soil restoration
  - community finance
participation_url: https://valid-org.example/join
sources:
  - source_id: bad-permission-about
    source_type: markdown
    canonical_url: https://valid-org.example/about
    title: About Valid Organisation
    permission_mode: unrestricted
    published_at: 2026-05-01
    snapshot_path: tests/fixtures/snapshots/valid-org-about.md
  - source_id: bad-permission-updates
    source_type: markdown
    canonical_url: https://valid-org.example/updates
    title: Valid Organisation Updates
    permission_mode: link-and-summarise
    published_at: null
    snapshot_path: tests/fixtures/snapshots/valid-org-updates.md
representative_questions:
  - What does Valid Organisation do?
---

# Bad Permission Fixture

Invalid on purpose: permission_mode is not one of the allowed values.
