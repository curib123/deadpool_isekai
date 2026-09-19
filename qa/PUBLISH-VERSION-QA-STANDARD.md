# Publish Version QA Standard

**Gate:** 11 — Publish Version QA  
**Owner:** A124 Publish Version QA Editor  
**Applies To:** Reader-facing chapter/volume copies derived from already-CANON manuscripts  
**Output State:** PUBLISH-READY or FAIL — RETURN TO PUBLICATION EDITOR

# 1. Purpose

Publish Version QA is the final reader-facing quality gate.

It exists **after canonization**.

Its job is not to rewrite story canon.

Its job is to verify that the publication copy:

- faithfully reproduces the approved canon manuscript;
- contains no repository/editorial metadata;
- is cleanly formatted for the target reading platform;
- preserves intentional paragraph rhythm, dialogue, emphasis and scene breaks;
- contains no accidental omissions, duplications or copy/paste corruption;
- does not introduce continuity, mystery, power, character or wording drift through publication cleanup.

# 2. Canon Source Rule

The authoritative source remains:

`manuscript/CH###-....md`

A publication copy is a **derived release artifact**.

It is never allowed to redefine:

- events;
- scene order;
- dialogue meaning;
- character knowledge;
- injuries;
- power use;
- mystery clues;
- F-ID state;
- ending beat;
- chapter title;
- canon final line.

If a desired publication edit changes meaning, characterization, pacing structure, lore, continuity or story content:

**STOP.**

Return the change to:

1. Manuscript / Prose Editor as appropriate;
2. Gate 9 Chapter QA;
3. Canon Librarian;
4. regenerate the publication copy from the newly approved canon manuscript;
5. rerun Gate 11.

Do not silently patch canon through the published version.

# 3. Allowed Publication-Only Changes

Gate 11 may approve presentation-only changes such as:

- removing repository status lines;
- removing word-count lines;
- removing QA file references;
- removing internal production headings not meant for readers;
- normalizing blank lines;
- normalizing platform-safe em dashes/apostrophes/quotation marks where meaning is unchanged;
- preserving or converting intentional italics/bold into the target platform's supported markup;
- normalizing scene-break symbols;
- correcting accidental double spaces;
- correcting accidental duplicate blank lines;
- platform-safe chapter-title formatting;
- platform-safe paragraph spacing.

Spelling or punctuation corrections are allowed **only when unquestionably non-substantive**.

If the correction can alter voice, emphasis, timing, interpretation or canon meaning, return it to Gate 9.

# 4. Forbidden Publish-Only Changes

Do not change only in the publication copy:

- names;
- locations;
- chronology;
- event order;
- dialogue content or intent;
- jokes;
- internal thoughts;
- POV;
- injuries;
- ability behavior;
- manifestation count;
- regeneration rules;
- System/lore wording;
- Hesk/lure logic;
- evidence chains;
- mystery/foreshadowing wording;
- F-ID clues;
- chapter endings;
- chapter titles;
- character relationships;
- worldbuilding facts;
- future-route hints.

Do not add:

- author's notes inside chapter prose unless explicitly approved;
- spoilers;
- QA notes;
- canon labels;
- repository filenames;
- Markdown production metadata;
- AI/editorial commentary;
- “Chapter Summary” text unless the publishing plan explicitly requires one.

# 5. Required Gate 11 Checks

## A. Source Integrity

- publication source chapter is CANON;
- source has Gate 9 PASS;
- chapter number matches;
- chapter title matches;
- publication copy was derived from the latest canon source;
- no older draft text survived;
- first paragraph matches canon meaning;
- final paragraph/final line matches canon meaning;
- no scene is missing;
- no scene is duplicated;
- no paragraphs are accidentally reordered.

## B. Canon Equivalence

The publication version must preserve:

- all story events;
- all dialogue;
- all character decisions;
- all injuries/consequences;
- all Play Logic uses and limits;
- all mystery clues;
- all established knowledge boundaries;
- all chapter handoffs.

A formatting-only diff is ideal.

Any semantic diff requires explicit review.

## C. Reader-Facing Cleanup

Remove publication-inappropriate repository metadata such as:

- `**Status:** ...`
- `**Word Count:** ...`
- `**Chapter QA:** ...`
- internal file references;
- QA/Gate notes;
- editorial comments;
- implementation notes.

Keep only reader-facing title and chapter prose unless the release format explicitly requires more.

## D. Typography / Formatting

Verify:

- chapter title is clean;
- dialogue quotation marks are paired;
- apostrophes are correct;
- em dashes are not corrupted;
- ellipses are intentional and consistent;
- italics/emphasis survive conversion;
- no raw Markdown markers remain unless supported by target platform;
- scene breaks are consistent;
- no accidental code fences;
- no broken entities/HTML;
- no duplicated punctuation caused by conversion.

## E. Paragraph / Mobile Readability

Verify:

- normal paragraphs remain multi-sentence where canon intended;
- intentional one-line impact paragraphs remain separate;
- dialogue remains readable;
- no giant wall of text was created by copy conversion;
- no every-sentence-new-line conversion was introduced;
- paragraph breaks do not change comedic or dramatic timing;
- mobile reading remains comfortable.

Do not “optimize” paragraphing in a way that changes canon prose rhythm.

## F. Internal Thought / Reader-Talk Integrity

Verify:

- private self-talk remains distinguishable from spoken dialogue;
- direct reader address remains exactly as canon intends;
- no automatic italics rule is imposed unless the canon source already marks the thought/emphasis or the project explicitly locks such formatting;
- quotation marks are not added around narration/internal thought;
- platform conversion does not accidentally turn narration into dialogue.

## G. Platform Safety

For WebNovel-style publication copies:

- no repository metadata;
- no unsupported formatting dependency required to understand the chapter;
- paragraph breaks survive plain-text paste;
- scene breaks remain visible after paste;
- title does not include internal CH-ID unless deliberately desired;
- no accidental duplicate chapter title inside body;
- no internal QA language appears to readers.

This gate checks presentation readiness, not WebNovel algorithm performance.

## H. Copyright / Reference Safety

Verify:

- no copied lyrics;
- no substantial copyrighted dialogue;
- pop-culture references remain brief/transformed/situational;
- publication cleanup did not expand a reference into protected source material.

## I. Continuity / Spoiler Safety

Verify:

- no later-chapter text was pasted into the current chapter;
- no future mystery answer appears;
- no next-destination information is introduced early;
- chapter ending still stops at its canon boundary.

# 6. Severity Rules

## CRITICAL

Examples:

- publication copy contains non-canon story events;
- chapter is derived from a non-canon/outdated draft;
- protected mystery leak;
- missing or duplicated scene that changes story;
- wrong chapter ending;
- wrong chapter pasted under title;
- semantic change to power, character, lore or chronology.

**Result: FAIL. Do not publish.**

## MAJOR

Examples:

- meaningful paragraph/dialogue omission;
- substantial formatting corruption;
- internal repository/QA material visible to readers;
- platform conversion changes internal-thought/dialogue meaning;
- chapter title mismatch;
- semantic punctuation/edit drift;
- duplicated prose block.

**Result: FAIL until corrected.**

## MINOR

Examples:

- isolated spacing issue;
- harmless double space;
- inconsistent scene-break glyph;
- non-semantic punctuation normalization;
- harmless reader-facing typographic inconsistency.

Minor defects must be corrected before final PASS unless explicitly waived and documented.

# 7. Publish Version Statuses

A publication artifact uses one of:

- **PUBLISH DRAFT — GATE 11 PENDING**
- **PUBLISH QA FAIL — REVISION REQUIRED**
- **PUBLISH-READY — GATE 11 PASS**
- **PUBLISHED — SOURCE LOCKED TO CANON SHA/REVISION**

`PUBLISHED` means released externally; it does not mean new canon.

# 8. Required QA Record

Each published chapter should receive:

`qa/publish/CH-###-PUBLISH-VERSION-QA.md`

Minimum record:

- chapter;
- canon source path;
- canon source revision/SHA when available;
- publication-copy path;
- target platform;
- review date;
- semantic-diff result;
- formatting result;
- metadata-removal result;
- title/ending verification;
- PASS/FAIL;
- corrections made.

For a completed volume, also create:

`qa/publish/VOLUME-001-PUBLISH-VERSION-QA.md`

after every chapter passes individually.

# 9. Volume Publish QA

A volume may be marked **PUBLISH-READY** only when:

- every chapter has Gate 11 PASS;
- all chapter titles and numbering are complete;
- no duplicate/missing chapter exists;
- publication order is CH-001 through final chapter;
- prologue/auxiliary content is explicitly categorized and not accidentally inserted into chapter order;
- all endings/handoffs remain canon-equivalent;
- final chapter matches the locked arc ending;
- volume-level front/back matter contains no spoiler or canon conflict;
- target-platform copy/paste behavior has been checked.

# 10. Gate 11 Decision Rule

**PASS** only when the published version is reader-ready and semantically equivalent to canon.

A Gate 11 PASS may authorize external posting.

It does **not** authorize canon changes.

If no publication copy exists yet:

**PENDING — CREATE PUBLISH VERSION FROM CANON SOURCE.**
