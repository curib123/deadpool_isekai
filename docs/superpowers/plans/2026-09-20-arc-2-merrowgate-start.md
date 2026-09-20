# Arc 2 — Merrowgate Start Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Start the Merrowgate Arc by synchronizing CH-027, “Salt in the Air,” to the current close-first-person story engine and revalidating it through Gate 9.

**Architecture:** Preserve the locked Volume 2 destination, chapter order, five-scene CH-027 architecture, and CH-028 handoff. This is a controlled prose synchronization, not an Arc 2 redesign. CH-028 remains blocked until CH-027 passes fresh Gate 9.

**Tech Stack:** Markdown manuscripts, scene architecture, QA records, PowerShell/ripgrep verification, Git.

**Spec:** volumes/VOLUME-002-MERROWGATE-ARCHITECTURE.md; scenes/CH-027-SALT-IN-THE-AIR-SCENE-ARCHITECTURE.md; chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md; manuscript/WRITING-RULES.md

## Global Constraints

- CH-027 is close first-person Red Jackal POV throughout.
- Preserve the five-scene route: travel costs, transfer fee, ordinary cargo hazard, salt/coastal transition, Merrowgate approach.
- Zero Play Logic, no major combat, no monster, no sabotage, no identity appraisal.
- No named Merrowgate cast, Cassian/Venn clue, F-ID, M-ID, charter politics, or protected mystery.
- Red remains unable to read Veyran; translation tokens translate speech only where present.
- Red follows transport-crew instruction during the hazard.
- Preserve CH-026 injury/recovery, ordinary resources, and solo departure.
- End before Merrowgate intake; CH-028 owns identity verification.
- Do not create a Volume 2 publication copy in this plan.

## Review Focus

- POV drift: verify every scene remains filtered through Red’s first-person perception.
- Boundary leakage: verify CH-028 intake and CH-029 reputation material do not enter CH-027.
- Power escalation: verify zero manifestations and no progression language.
- Travel plausibility: verify multiple-day road/river movement without unsupported distance or new named city.
- Handoff integrity: verify the final beat points to public intake and CH-028.

---

### Task 1: Rewrite CH-027

**Files:**
- Modify: manuscript/CH027-SALT-IN-THE-AIR.md
- Read: manuscript/CH026-BEFORE-THEY-DECIDE-WHAT-I-AM.md
- Read: scenes/CH-027-SALT-IN-THE-AIR-SCENE-ARCHITECTURE.md
- Read: chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md
- Read: manuscript/WRITING-RULES.md

**Produces:** Current CH-027 prose with current metadata, first-person voice, five-scene event order, zero Play Logic, and a direct CH-028 handoff.

- [ ] Read the current draft, CH-026 ending, locked scene architecture, roadmap, and writing rules.
- [ ] Rewrite the superseded close-third prose into immediate first-person Red narration without changing the approved event sequence.
- [ ] Preserve: shrinking travel resources, unreadable writing, residual soreness, one ordinary cargo-transfer hazard, no named cast, no antagonist clue, and the Merrowgate approach ending.
- [ ] Update status, revision date, and word count after the prose is final.
- [ ] Run a manual prose review plus:

  rg -n -i "Great Design|Savael|Exterior Needle|Eidrathi|Exception Covenant|Stage II|level progression|finite manifestation" manuscript/CH027-SALT-IN-THE-AIR.md

  git diff --check

  Expected: zero forbidden-term hits and zero whitespace errors.
- [ ] Commit with:

  git add manuscript/CH027-SALT-IN-THE-AIR.md
  git commit -m "rewrite: synchronize CH-027 to current story engine"

### Task 2: Fresh Gate 9 Revalidation

**Files:**
- Modify: qa/CH-027-GATE-9-CHAPTER-QA.md
- Read: qa/CH-027-PRE-MANUSCRIPT-SCENE-QA.md
- Read: qa/QA-GATES.md
- Read: qa/BATTLE-SCENE-QA-STANDARD.md
- Read: qa/SCENE-QA-STANDARD.md

**Produces:** A current Gate 9 record describing the synchronized prose rather than the superseded draft.

- [ ] Recount the chapter and compare all five scenes for event order, cast limits, power count, route, injury state, and ending.
- [ ] Recheck POV, chapter purpose, travel, language, recovery, hazard, power, mystery, cast, antagonist, continuity, and CH-028 handoff.
- [ ] Search for unauthorized leakage:

  rg -n -i "Iria Voss|Samir Kesran|Nessa Quill|Dalen Marr|Cassian Venn|Venn|Harbor Council|charter|sabotage|identity appraisal|F-010|M-002|M-011" manuscript/CH027-SALT-IN-THE-AIR.md

  Expected: no unauthorized named cast, antagonist, political, appraisal, F-ID, or M-ID material.
- [ ] Update the Gate 9 record with current evidence, date, word count, and final PASS.
- [ ] Commit with:

  git add qa/CH-027-GATE-9-CHAPTER-QA.md
  git commit -m "qa: revalidate CH-027 Merrowgate opening"

### Task 3: Synchronize Arc 2 State

**Files:**
- Modify only if required: continuity/VOLUME-002-KNOWLEDGE-STATE.md
- Modify: planning/STORY-PLANNING.md
- Modify: series/ROADMAP.md

**Produces:** Consistent current-state records declaring CH-027 current and CH-028 the only next authorized Gate 8 step.

- [ ] Search continuity, planning, and roadmap records for CH-027, CH-028, STALE, REVALIDATION REQUIRED, CURRENT, and Gate 9.
- [ ] Preserve explicitly historical notes; update only contradictory current-state lines.
- [ ] Set CH-027 to current close-first-person / Gate 9 PASS and keep CH-028 paused pending Detailed Scene Architecture / Gate 8.
- [ ] Verify with:

  rg -n -i "CH-027|CH-028|STALE|REVALIDATION REQUIRED|Gate 9|Gate 8" continuity/VOLUME-002-KNOWLEDGE-STATE.md planning/STORY-PLANNING.md series/ROADMAP.md

  Expected: current entries agree and CH-028 is the sole next step.
- [ ] Commit the smallest synchronized state update.

### Task 4: Final Handoff Verification

**Files:** Read the rewritten manuscript, fresh Gate 9 record, scene architecture, and Volume 2 roadmap.

- [ ] Verify current title, word count, five-scene alignment, zero manifestations, zero new F-ID/M-ID, cast boundary, and final handoff.
- [ ] Confirm no CH-028 manuscript or Volume 2 publication copy was created.
- [ ] Confirm the next authorized step is CH-028 Detailed Scene Architecture → Gate 8.

## Completion Contract

Arc 2 start is complete only when CH-027 is current close-first-person prose, fresh Gate 9 PASS is recorded, Arc 2 state files agree, no later chapter was drafted, and CH-028 is the next authorized step.
