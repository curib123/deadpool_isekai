# Arc 1 Official QA Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the user-provided 40-section Official Arc 1 QA Checklist to Greywake CH-001 through CH-026, repair evidence-backed weaknesses with the smallest effective change, and synchronize Gate 9, Battle/Scene QA, Gate 10, and Gate 11 records.

**Architecture:** The pass is evidence-first. A single authoritative checklist record will map every checklist section to current manuscript, scene, continuity, battle, mystery, and publication evidence. Documentation contradictions will be repaired at the earliest stale record; prose will be changed only when the checklist identifies a real narrative weakness, and every such change will be followed through downstream QA and publication equivalence.

**Tech Stack:** Markdown canon/QA records, PowerShell read-only audit commands, `rg`, Git object hashes, `git diff --check`, and repository history. No application test runner exists in this Markdown-only workspace.

**Spec:** `docs/superpowers/specs/2026-09-20-arc-1-official-qa-repair-design.md`

## Global Constraints

- Scope is Volume 1 / Greywake / CH-001 through CH-026; CH-027 and Volume 2 remain excluded.
- All 40 checklist sections must appear in `qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md`.
- Every `WEAK` or `MISSING` status must have an immediately adjacent `FIX:` line using `Problem → Cause → Best Chapter → Smallest Effective Fix → Continuity Check → Re-QA`.
- Red remains already overpowered; tension comes from objectives, information, restraint, consequences, and other actors.
- Battle variety is situational; no artificial 1v4, new power, character, faction, tragedy, or filler chapter may be added to satisfy a checkbox.
- Publication copies may receive presentation-only changes; any semantic change returns to the manuscript and Gate 9.
- A final claim of completion requires fresh verification evidence and a clean working tree except for explicitly documented stale external worktree links.

## Review Focus

- Mandatory checklist sections marked `PASS` without direct evidence: the audit record must cite chapter/scene lines or QA records for every mandatory result.
- Historical QA prose that contradicts the current first-person canon: current status and authority notices must be separated from historical records rather than silently treated as current.
- Publication records that claim current Gate 11 while carrying stale source revisions: source and publication Git object IDs must be refreshed and body equivalence rechecked.
- Great-battle claims that rely on topology labels alone: CH-022–CH-024 must retain geography, independent supporting-cast turns, escalation, and lasting consequences in prose.
- Mystery and knowledge-state overreach: the final audit must confirm no protected truth (`Soul Drift`, `Great Design`, `Savael`, `Exterior Needle`, or Eidrathi truth) leaks into CH-001–CH-026.

## File Map

- Create: `qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md` — authoritative 40-section checklist record and final gate result.
- Modify: `qa/VOLUME-001-GREYWAKE-OVERPOWERED-RETCON-GATE-10-REVALIDATION.md` — label obsolete POV-retcon language as historical and point current Arc 1 approval to the new record.
- Modify: `qa/publish/VOLUME-001-PUBLISH-VERSION-QA.md` — synchronize aggregate Gate 11 status with current first-person canon and the new checklist record.
- Modify: `qa/publish/CH-017-PUBLISH-VERSION-QA.md` through `qa/publish/CH-026-PUBLISH-VERSION-QA.md` — refresh current source/copy revision metadata and preserve unchanged reader-facing bodies.
- Modify only if evidence requires it: `manuscript/CH001...CH026`, `scenes/CH-001...CH-026`, chapter Gate 9 records, `qa/VOLUME-001-GREYWAKE-BATTLE-SCENE-AUDIT.md`, `qa/VOLUME-001-GREYWAKE-GATE-10-CANON-REVALIDATION.md`, `continuity/VOLUME-001-KNOWLEDGE-STATE.md`, `mysteries/MYSTERY-BIBLE.md`, and the relevant roadmap/architecture record.

### Task 1: Build the evidence-backed 40-section Arc 1 audit

**Files:**
- Create: `qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md`
- Read: `C:\Users\studi\.codex\attachments\28a84e58-85aa-45c0-8885-7770db3eeb00\pasted-text.txt`
- Read: `studio/STUDIO-ARCHITECTURE.md`, `series/SERIES-CONSTITUTION.md`, `world/WORLD-BIBLE.md`, `systems/SYSTEMS-BIBLE.md`, `characters/CHARACTER-BIBLE.md`, `mysteries/MYSTERY-BIBLE.md`, `planning/STORY-PLANNING.md`, `manuscript/WRITING-RULES.md`, `continuity/CONTINUITY-BIBLE.md`, `qa/QA-GATES.md`, `qa/PUBLISH-VERSION-QA-STANDARD.md`, `published/README.md`, and `series/ROADMAP.md`
- Read: all `manuscript/CH001...CH026`, `scenes/CH-001...CH-026`, chapter Gate 9 records, publication QA records, Greywake Gate 6/7/8/10/11 records, continuity ledger, mystery registry, and battle audit.

**Interfaces:**
- Consumes: current canon hierarchy and user checklist.
- Produces: one complete checklist record with one status per item/section, direct evidence, and the final 10-point gate result.

- [ ] **Step 1: Establish the chapter and release baseline.**

Run from the repository root:

```powershell
$arc = 1..26 | ForEach-Object { '{0:D3}' -f $_ }
$manuscripts = rg --files manuscript | Where-Object { $_ -match 'CH(00[1-9]|0[12][0-9]|026)-' }
$published = rg --files published/volume-001 | Where-Object { $_ -match 'CH(00[1-9]|0[12][0-9]|026)-' }
if ($manuscripts.Count -ne 26) { throw "Expected 26 Arc 1 manuscripts; found $($manuscripts.Count)" }
if ($published.Count -ne 26) { throw "Expected 26 Arc 1 publication copies; found $($published.Count)" }
if ((rg --files qa | Where-Object { $_ -match 'CH-0(0[1-9]|1[0-9]|2[0-6])-GATE-9-CHAPTER-QA\.md$' }).Count -ne 26) { throw 'Expected 26 current chapter Gate 9 records' }
```

Expected result: all three baseline checks pass; CH-027 is not counted.

- [ ] **Step 2: Read each checklist section against direct story evidence.** For sections 1–36, record the exact chapters/scenes or locked QA records that satisfy each bullet. Treat existing aggregate claims as evidence only after checking the underlying manuscript. Use `PASS` only when the requirement is present; use `N/A` only for optional battle forms or intentionally inapplicable dark-turn items with a reason.

- [ ] **Step 3: Record every non-PASS result with an adjacent `FIX:` line.** The line must contain all six repair-rule fields in order: problem, cause, best chapter, smallest effective fix, continuity check, and re-QA. No `WEAK` or `MISSING` may be left as a bare status.

- [ ] **Step 4: Run the protected-mystery and progression-drift scan before choosing narrative fixes.**

```powershell
$scan = rg -n -i 'Soul Drift|Great Design|Savael|Exterior Needle|Eidrathi|Stage [IVX]+|progression tier|finite manifestation|stamina budget|power bar' manuscript/CH0*.md
if ($scan) { $scan }
```

Expected result: no protected writer-truth leaks or forbidden progression language in CH-001 through CH-026; any hit must be reviewed against the locked canon before the checklist can pass.

- [ ] **Step 5: Run the narrative self-review.** Confirm that any proposed prose fix targets an existing scene, has a named chapter, changes a real weakness, and does not add a new chapter, named character, power, faction, or forced battle topology.

- [ ] **Step 6: Commit the initial evidence record.**

```powershell
git add -- 'qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md'
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m 'qa: audit Greywake against Arc 1 checklist'
```

### Task 2: Repair stale authority and publication metadata

**Files:**
- Modify: `qa/VOLUME-001-GREYWAKE-OVERPOWERED-RETCON-GATE-10-REVALIDATION.md`
- Modify: `qa/publish/VOLUME-001-PUBLISH-VERSION-QA.md`
- Modify: `qa/publish/CH-017-PUBLISH-VERSION-QA.md` through `qa/publish/CH-026-PUBLISH-VERSION-QA.md`
- Modify: `qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md`

**Interfaces:**
- Consumes: Task 1 evidence record and current manuscript/publication files.
- Produces: current-status documents that no longer treat the superseded third-person retcon as the active canon and publication records whose revision metadata matches Git.

- [ ] **Step 1: Preserve historical context but make current status unambiguous.** In the aggregate Gate 10 overpowered-retcon record, retain the historical explanation while adding a prominent current-authority notice: CH-001 through CH-026 are current close-first-person canon, and current Arc 1 status is governed by `qa/VOLUME-001-GREYWAKE-GATE-10-CANON-REVALIDATION.md` plus the new official checklist. Do not rewrite historical audit facts as if they were performed under the current checklist.

- [ ] **Step 2: Synchronize the aggregate Gate 11 record.** Replace the stale “publication set is no longer release-authoritative” notice with the verified current state: CH-001 through CH-026 publication bodies are derived from the current first-person canon, body-equivalent, and individually subject to Gate 11. Retain the individual refresh history as historical context and link the official checklist.

- [ ] **Step 3: Refresh CH-017 through CH-026 publication QA metadata.** For each pair, calculate the exact current Git object IDs:

```powershell
for ($n = 17; $n -le 26; $n++) {
  $id = '{0:D3}' -f $n
  $source = Get-ChildItem manuscript | Where-Object Name -match "^CH$id-.*\.md$" | Select-Object -First 1
  $copy = Get-ChildItem published/volume-001 | Where-Object Name -match "^CH$id-.*\.md$" | Select-Object -First 1
  Write-Output "CH-$id source=$($source.Name) source_sha=$(git hash-object -- $source.FullName) copy_sha=$(git hash-object -- $copy.FullName)"
}
```

Update only the revision metadata, review date, and wording required to identify the current source. Add `Publication Copy SHA` where absent. Do not change reader-facing prose.

- [ ] **Step 4: Verify every Arc 1 publication record.** For CH-001 through CH-026, compare manuscript and publication bodies after removing repository-only metadata and the publication title line. Confirm no paragraph, dialogue block, scene break, ending, battle geography, mystery clue, or knowledge-state change occurred. The expected result is 26/26 body-equivalent and 26/26 current source SHA/copy SHA records.

- [ ] **Step 5: Update the official checklist’s publication and authority sections, then commit.**

```powershell
git diff --check
git add -- 'qa/VOLUME-001-GREYWAKE-OVERPOWERED-RETCON-GATE-10-REVALIDATION.md' 'qa/publish/VOLUME-001-PUBLISH-VERSION-QA.md' 'qa/publish/CH-017-PUBLISH-VERSION-QA.md' 'qa/publish/CH-018-PUBLISH-VERSION-QA.md' 'qa/publish/CH-019-PUBLISH-VERSION-QA.md' 'qa/publish/CH-020-PUBLISH-VERSION-QA.md' 'qa/publish/CH-021-PUBLISH-VERSION-QA.md' 'qa/publish/CH-022-PUBLISH-VERSION-QA.md' 'qa/publish/CH-023-PUBLISH-VERSION-QA.md' 'qa/publish/CH-024-PUBLISH-VERSION-QA.md' 'qa/publish/CH-025-PUBLISH-VERSION-QA.md' 'qa/publish/CH-026-PUBLISH-VERSION-QA.md' 'qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md'
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m 'qa: synchronize Greywake Gate 10 and Gate 11 records'
```

### Task 3: Apply only evidence-backed narrative repairs

**Files:**
- Modify only the exact manuscript/scene/continuity/mystery files named by a Task 1 `WEAK` or `MISSING` result.
- Candidate existing beats to inspect first: CH-001–CH-003 hook/anomaly, CH-005–CH-007 power/consequence reveal, CH-008–CH-014 investigation/midpoint, CH-015–CH-021 mistake/counter-plan, CH-022–CH-024 great battle/climax, and CH-025–CH-026 aftermath/resolution/Arc 2 hook.

**Interfaces:**
- Consumes: Task 1 repair lines and locked bibles.
- Produces: smallest effective prose or scene-architecture corrections, with no unsupported story expansion.

- [ ] **Step 1: Select a repair only when the checklist evidence names a real defect.** A stale QA sentence is fixed in the QA record, not in prose. A prose fix must identify a missing/weak reader-facing event, line, reaction, decision, consequence, battle beat, or handoff in an existing scene.

- [ ] **Step 2: Implement the smallest multi-purpose change.** Prefer an existing conversation, battle beat, reaction, or aftermath paragraph that can simultaneously improve checklist dimensions. Preserve first-person Red POV, stable Red identity, character knowledge, mystery firewall, current battle topology, and chapter ending unless the locked authority record explicitly requires a change.

- [ ] **Step 3: Update the owning scene architecture and continuity record immediately after each prose change.** The scene card must still state objective, participants, knowledge boundary, turn, consequence, and next-scene handoff. Continuity must reflect any changed injury, item, relationship, travel position, clue, or institutional consequence.

- [ ] **Step 4: Run chapter-level checks for every changed chapter.** Re-read the full chapter, its scene architecture, its Gate 8 record, its Gate 9 record, and downstream chapters that consume its knowledge or consequences. Re-run the battle standard for any changed action scene.

- [ ] **Step 5: Update the official checklist’s affected rows with the repair chain and evidence.** If the repair resolves the issue, change the status to `PASS`; if the issue remains, retain `WEAK`/`MISSING` with a directly adjacent actionable `FIX:` and explain why it is intentionally deferred.

### Task 4: Re-run Arc 1 continuity, battle, Gate 9, and Gate 10 QA

**Files:**
- Modify: affected chapter Gate 9 and Gate 8 records, `qa/VOLUME-001-GREYWAKE-BATTLE-SCENE-AUDIT.md`, `qa/VOLUME-001-GREYWAKE-GATE-10-CANON-REVALIDATION.md`, and `qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md`
- Read: `continuity/VOLUME-001-KNOWLEDGE-STATE.md`, `continuity/CONTINUITY-BIBLE.md`, `qa/BATTLE-SCENE-QA-STANDARD.md`, `qa/SCENE-QA-STANDARD.md`, and all current CH-001–CH-026 Gate 9 records.

**Interfaces:**
- Consumes: current manuscripts and any Task 3 repairs.
- Produces: synchronized chapter/scene/battle/volume records and an evidence-backed Gate 10 decision.

- [ ] **Step 1: Re-run continuity in chapter order.** Verify timeline, travel, character knowledge, injuries, items, relationships, locations, promises/debts, foreshadowing, and locked system rules. Any contradiction must be repaired at its earliest source before downstream statuses are changed.

- [ ] **Step 2: Re-run the battle variety audit.** Confirm the existing nine Greywake battle/action entries retain distinct topologies, objectives, terrain, participant sets, Red roles, independent supporting-cast decisions, reversals, and lasting consequences. Confirm CH-022–CH-024 remains a continuous three-part climax and does not depend on a new 1v4 or artificial encounter.

- [ ] **Step 3: Re-run Gate 9 for all 26 chapters.** Confirm every scene has purpose/turn/handoff, action has geography and consequence, Red’s serious switch is restraint removal rather than a power-up, comedy does not erase damage, and mystery/knowledge boundaries are correct. A changed chapter receives a full record refresh; unchanged chapters receive a dated revalidation note only if required by the QA record format.

- [ ] **Step 4: Re-run Gate 10.** Update current word totals, POV, chapter range, battle audit link, continuity evidence, mystery/foreshadowing evidence, resolution, aftermath, and Arc 2 hook. Leave historical audit sections labeled historical and ensure no stale sentence can be read as the current decision.

- [ ] **Step 5: Commit the canon QA synchronization.**

```powershell
git diff --check
# Add only the exact CH-001...CH-026 records changed by the repair; never use a broad
# CH-* glob here because CH-027 is explicitly outside this plan.
git add -- 'qa/CH-001-GATE-9-CHAPTER-QA.md' 'qa/CH-002-GATE-9-CHAPTER-QA.md' 'qa/CH-003-GATE-9-CHAPTER-QA.md' 'qa/CH-004-GATE-9-CHAPTER-QA.md' 'qa/CH-005-GATE-9-CHAPTER-QA.md' 'qa/CH-006-GATE-9-CHAPTER-QA.md' 'qa/CH-007-GATE-9-CHAPTER-QA.md' 'qa/CH-008-GATE-9-CHAPTER-QA.md' 'qa/CH-009-GATE-9-CHAPTER-QA.md' 'qa/CH-010-GATE-9-CHAPTER-QA.md' 'qa/CH-011-GATE-9-CHAPTER-QA.md' 'qa/CH-012-GATE-9-CHAPTER-QA.md' 'qa/CH-013-GATE-9-CHAPTER-QA.md' 'qa/CH-014-GATE-9-CHAPTER-QA.md' 'qa/CH-015-GATE-9-CHAPTER-QA.md' 'qa/CH-016-GATE-9-CHAPTER-QA.md' 'qa/CH-017-GATE-9-CHAPTER-QA.md' 'qa/CH-018-GATE-9-CHAPTER-QA.md' 'qa/CH-019-GATE-9-CHAPTER-QA.md' 'qa/CH-020-GATE-9-CHAPTER-QA.md' 'qa/CH-021-GATE-9-CHAPTER-QA.md' 'qa/CH-022-GATE-9-CHAPTER-QA.md' 'qa/CH-023-GATE-9-CHAPTER-QA.md' 'qa/CH-024-GATE-9-CHAPTER-QA.md' 'qa/CH-025-GATE-9-CHAPTER-QA.md' 'qa/CH-026-GATE-9-CHAPTER-QA.md' 'qa/VOLUME-001-GREYWAKE-BATTLE-SCENE-AUDIT.md' 'qa/VOLUME-001-GREYWAKE-GATE-10-CANON-REVALIDATION.md' 'qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md'
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m 'qa: revalidate Greywake continuity battle and Gate 10'
```

### Task 5: Re-run Gate 11 and close the official checklist

**Files:**
- Modify: `qa/publish/CH-001...CH-026-PUBLISH-VERSION-QA.md` only where evidence changed
- Modify: `qa/publish/VOLUME-001-PUBLISH-VERSION-QA.md`
- Modify: `qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md`

**Interfaces:**
- Consumes: canon manuscripts and final Gate 9/Gate 10 results.
- Produces: a reader-facing release decision that is canon-equivalent and a closed Arc 1 checklist.

- [ ] **Step 1: Re-run individual Gate 11 checks.** For every CH-001 through CH-026 publication copy, confirm source is current CANON/Gate 9 PASS, title matches, metadata is removed from reader text, body order and semantic meaning match, no protected mystery leaks, formatting is readable, and no battle geography or consequence wording changed.

- [ ] **Step 2: Re-run aggregate Gate 11.** Confirm 26/26 current source revisions, 26/26 publication copy revisions, 26/26 body-equivalent copies, and no unresolved CRITICAL/MAJOR publication defect. Do not mark publication-ready if a semantic change requires a manuscript return.

- [ ] **Step 3: Close the 40-section checklist.** Ensure all sections 1–40 are present; every status is exactly `PASS`, `WEAK`, `MISSING`, or `N/A`; every non-PASS has an adjacent `FIX:` line; the ten-point gate reports an honest result; and the record lists remaining intentional `N/A` items without treating them as failures.

- [ ] **Step 4: Run final repository verification.**

```powershell
git diff --check
if (rg -n '^Status: (WEAK|MISSING)$|^\*\*Status:\*\* (WEAK|MISSING)$' 'qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md') { throw 'Use section-level statuses or inspect remaining non-PASS results' }
$required = 1..40 | ForEach-Object { "# $_\." }
$checklist = Get-Content -Raw 'qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md'
if (($checklist -split "`n" | Where-Object { $_ -match '^## (\d+)[\.) ]' }).Count -ne 40) { throw 'Expected exactly 40 checklist sections' }
if ((rg -n 'Soul Drift|Great Design|Savael|Exterior Needle|Eidrathi' manuscript/CH0*.md)) { throw 'Protected mystery leak remains in Arc 1 manuscripts' }
git status --short
git log -5 --oneline
```

Expected result: the checklist passes its structural validation, the final QA evidence reports exact counts, no new Arc 1 prose was added without a repair line, and the working tree is clean apart from the known stale external worktree-link condition if it remains.

- [ ] **Step 5: Commit the final release QA.**

```powershell
git add -- 'qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md' 'qa/publish/VOLUME-001-PUBLISH-VERSION-QA.md' 'qa/publish/CH-001-PUBLISH-VERSION-QA.md' 'qa/publish/CH-002-PUBLISH-VERSION-QA.md' 'qa/publish/CH-003-PUBLISH-VERSION-QA.md' 'qa/publish/CH-004-PUBLISH-VERSION-QA.md' 'qa/publish/CH-005-PUBLISH-VERSION-QA.md' 'qa/publish/CH-006-PUBLISH-VERSION-QA.md' 'qa/publish/CH-007-PUBLISH-VERSION-QA.md' 'qa/publish/CH-008-PUBLISH-VERSION-QA.md' 'qa/publish/CH-009-PUBLISH-VERSION-QA.md' 'qa/publish/CH-010-PUBLISH-VERSION-QA.md' 'qa/publish/CH-011-PUBLISH-VERSION-QA.md' 'qa/publish/CH-012-PUBLISH-VERSION-QA.md' 'qa/publish/CH-013-PUBLISH-VERSION-QA.md' 'qa/publish/CH-014-PUBLISH-VERSION-QA.md' 'qa/publish/CH-015-PUBLISH-VERSION-QA.md' 'qa/publish/CH-016-PUBLISH-VERSION-QA.md' 'qa/publish/CH-017-PUBLISH-VERSION-QA.md' 'qa/publish/CH-018-PUBLISH-VERSION-QA.md' 'qa/publish/CH-019-PUBLISH-VERSION-QA.md' 'qa/publish/CH-020-PUBLISH-VERSION-QA.md' 'qa/publish/CH-021-PUBLISH-VERSION-QA.md' 'qa/publish/CH-022-PUBLISH-VERSION-QA.md' 'qa/publish/CH-023-PUBLISH-VERSION-QA.md' 'qa/publish/CH-024-PUBLISH-VERSION-QA.md' 'qa/publish/CH-025-PUBLISH-VERSION-QA.md' 'qa/publish/CH-026-PUBLISH-VERSION-QA.md'
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m 'qa: close Greywake Arc 1 official checklist'
```
