# Published Versions

This directory is for **reader-facing release copies** derived from already-CANON manuscripts.

It is intentionally separate from `manuscript/`.

# Source of Truth

The canon source is always:

`manuscript/CH###-....md`

A file in `published/` is a release artifact, not a second canon source.

If publication cleanup reveals a real prose/story problem that requires a semantic change:

1. edit the canon manuscript through the proper editorial workflow;
2. rerun Gate 9;
3. recanonize;
4. regenerate the publication copy;
5. rerun Gate 11.

Never fix story canon only inside `published/`.

# Recommended Layout

```text
published/
  volume-001/
    CH001-WRONG-FOREST-WRONG-WORLD.md
    CH002-UNDEFINED.md
    ...
    CH026-BEFORE-THEY-DECIDE-WHAT-I-AM.md
```

# Reader-Facing Chapter Format

Default publication chapter:

```text
Chapter 1 — Wrong Forest, Wrong World

[chapter prose only]
```

Do not include reader-visible repository metadata such as:

- CANON status;
- Gate numbers;
- word count;
- QA path;
- source SHA;
- internal CH-ID unless deliberately wanted in the display title;
- production notes.

Source revision information belongs in the Gate 11 QA record, not in the reader-facing chapter.

# Publication Status

A file in this directory must use one of these workflow states in its QA record:

- PUBLISH DRAFT — GATE 11 PENDING
- PUBLISH QA FAIL — REVISION REQUIRED
- PUBLISH-READY — GATE 11 PASS
- PUBLISHED — SOURCE LOCKED TO CANON REVISION

The visible published prose itself should not display those labels.

# WebNovel-Oriented Rules

For WebNovel copy/paste:

- preserve clean paragraph breaks;
- do not depend on unsupported Markdown for meaning;
- keep intentional scene breaks visible in plain text;
- remove internal production metadata;
- do not auto-italicize every internal thought;
- preserve the canon distinction between narration, private self-talk, reader-talk and spoken dialogue;
- verify the first and final paragraphs after pasting;
- verify no paragraph was duplicated or omitted;
- keep Author's Thoughts separate from chapter prose unless intentionally written for that field.

# Required QA

Every release chapter must pass:

`Gate 11 — Publish Version QA`

using:

`qa/PUBLISH-VERSION-QA-STANDARD.md`

Chapter QA records belong under:

`qa/publish/`

A completed volume also receives a volume-level Publish Version QA.


# Primary WebNovel Opening Sequence

For contract-focused / reader-acquisition release, use:

1. `published/SYNOPSIS.md`
2. `published/volume-001/CH001-WRONG-FOREST-WRONG-WORLD.md`
3. continue CH-002 onward in numbered order.

The existing `published/PROLOGUE-THE-WRONG-PERSON.md` is retained as an **optional alternate/bonus prologue**, but it must **not** precede CH-001 in the primary WebNovel sequence because its explosion/white-space/arrival material overlaps CH-001.

This keeps CH-001 as the first dramatic reading unit and avoids making a new reader experience the opening twice.
