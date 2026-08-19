---
organisation_id: bad-source-id
display_name: Valid Organisation
profile: A public interest organisation working on soil restoration.
themes:
  - soil restoration
  - community finance
participation_url: https://valid-org.example/join
sources:
  - source_id: other-org-about
    source_type: markdown
    canonical_url: https://valid-org.example/about
    title: About Valid Organisation
    permission_mode: experiment-use
    published_at: 2026-05-01
    snapshot_path: tests/fixtures/snapshots/valid-org-about.md
  - source_id: bad-source-id-updates
    source_type: markdown
    canonical_url: https://valid-org.example/updates
    title: Valid Organisation Updates
    permission_mode: link-and-summarise
    published_at: null
    snapshot_path: tests/fixtures/snapshots/valid-org-updates.md
representative_questions:
  - What does Valid Organisation do?
---

# Bad Source Id Fixture

Invalid on purpose: the first source_id does not start with organisation_id.
