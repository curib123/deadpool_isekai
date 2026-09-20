# Battle and Scene OA Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a reusable battle/scene OA contract, document Merrowgate's complete battle/action coverage, and connect those assignments to the locked chapter roadmap without changing canon prose.

**Architecture:** Keep the existing Battle Scene QA Standard as the governing rule. Add one reusable planning template, one Merrowgate arc audit/map containing full encounter cards, and lightweight chapter-level assignments in the Merrowgate roadmap. The audit distinguishes `BATTLE`, `HAZARD ACTION`, and `NO BATTLE`, so topology variety is documented without forcing combat into non-combat chapters.

**Tech Stack:** Markdown, PowerShell, ripgrep, Git.

**Spec:** `docs/superpowers/specs/2026-09-20-battle-scene-oa-design.md`

## Global Constraints

- “Keep non-combat chapters non-combat; never add a fight just to hit a quota.”
- “Red is already overwhelmingly powerful; tension comes from restraint, information, simultaneous objectives, positioning, consequences, and what an instant solution would damage or reroute.”
- “A serious Red beat is restraint dropping, never a new power stage.”
- “Supporting characters retain their specialties and independent agency.”
- “Battle topology must arise from the situation. The template records variety; it does not mandate every topology in every arc.”
- “The existing `qa/BATTLE-SCENE-QA-STANDARD.md` remains the governing quality standard.”
- “Detailed scene architecture remains a Gate 8 deliverable for the active chapter.”
- “No current manuscript, published copy, chapter order, destination, character identity, power model, or locked mystery state changes as part of this planning revision.”

## Review Focus

- A chapter listed as `NO BATTLE` must not receive a battle ID or combat assignment; verify the explicit Merrowgate classification list in Task 3.
- Every `BATTLE` or `HAZARD ACTION` card must include all required fields, including protected targets, topology change, cost, and handoff; verify the card scan in Task 2.
- The CH-047→CH-048 great battle must remain multi-front and coalition-dependent rather than collapsing into Red versus Cassian; verify the great-battle checks in Task 2.
- The natural 2v4/1v4 private-security interception must affect tactics and objectives rather than exist as decorative numbers; verify its card wording and topology audit in Task 2.
- Only planning/QA/roadmap files may change; verify the changed-file allowlist and manuscript/publication scan in Task 4.

## File Map

- Create `planning/BATTLE-SCENE-OA-TEMPLATE.md`: reusable arc, chapter, matchup-card, scene-beat, and gate-handoff contract for future destination arcs.
- Create `qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md`: Merrowgate's authoritative battle/action map, detailed cards, topology audit, great-battle design, agency checks, and planning-only status.
- Modify `chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md`: add chapter-level Battle/Scene OA assignments and explicit non-combat classifications while preserving all existing chapter locks.
- Do not modify `manuscript/`, `published/`, `characters/`, `mysteries/`, `continuity/`, or existing prose QA files.

---

### Task 1: Create the reusable Battle / Scene OA template

**Files:**
- Create: `planning/BATTLE-SCENE-OA-TEMPLATE.md`
- Reference: `qa/BATTLE-SCENE-QA-STANDARD.md`, `qa/SCENE-QA-STANDARD.md`, `qa/QA-GATES.md`

**Interfaces:**
- Consumes: the existing Battle Scene QA required fields and Gate 6–10 responsibilities.
- Produces: a copyable Markdown contract whose field names match the Merrowgate audit and future arc records.

- [ ] **Step 1: Record the template contract**

Write the document with these sections and exact field names:

```markdown
# Battle / Scene OA Template

**Arc:**
**Destination:**
**Status:** PLANNING ONLY / GATE 6 / GATE 7 / GATE 8 / GATE 9 / GATE 10
**Governing standards:** `qa/BATTLE-SCENE-QA-STANDARD.md`; `qa/SCENE-QA-STANDARD.md`

## 1. Arc Battle Composition Map

| Battle/Action ID | Chapter | Classification | Matchup | Scale | Topology | Terrain | Objective | Red's Role | Decisive Supporting Roles | Turning Point | Outcome | Cost |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 2. Chapter Assignment

**Chapter / Scene ID:**
**Classification:** BATTLE / HAZARD ACTION / NO BATTLE
**Battle / Action ID:**
**Scale:** MINOR / MAJOR / CLIMAX / NOT APPLICABLE
**Matchup identity:**
**Protected targets / non-combatants:**
**Initial numerical topology:**
**Topology changes:**
**Terrain / action geography:**
**Primary objective:**
**Secondary objective:**
**Why immediate overwhelming force is not the actual objective:**
**Red's role:**
**Decisive supporting roles:**
**Opponent / hazard behavior:**
**Turning point:**
**Resolution:**
**Cost / irreversible consequence:**
**Handoff:**

## 3. Scene Beat Order

1. Orientation — who, where, and what matters.
2. First contact — the first tactic or failure.
3. Response — opposition adapts.
4. Complication — numbers, terrain, or objective changes.
5. Choice — a character chooses which objective matters.
6. Turning point — the battle/action state changes.
7. Resolution — defeat, escape, hold, rescue, delay, capture, route secured, or another earned result.
8. Cost — injury, lost time, damaged infrastructure, political consequence, exposed ability, enemy escape, or lost evidence.
9. Handoff — the encounter creates the next scene.

## 4. Arc-Level Checks

- [ ] At least one major/great battle materially changes the arc.
- [ ] Minor encounters perform at least two story functions each.
- [ ] Three or more distinct topologies or action structures appear where the destination supports them.
- [ ] At least one battle has a decisive non-Red actor.
- [ ] At least one battle's primary objective is not defeating the opposing force.
- [ ] Terrain, civilians, evidence, escort, infrastructure, timing, politics, ecology, or simultaneous objectives materially complicate at least one encounter.
- [ ] No `NO BATTLE` chapter receives a combat assignment.

## 5. Gate Handoff

- Gate 6: arc map exists before climax drafting.
- Gate 7: every battle/action chapter has a classification and topology assignment.
- Gate 8: detailed matchup card and action geography are locked for the active chapter.
- Gate 9: prose preserves participant roles, geography, topology, objective, and consequence.
- Gate 10: arc variety and lasting-consequence audit passes.
```

- [ ] **Step 2: Check the template against the governing standards**

Run:

```powershell
rg -n "Battle/Action ID|Classification|Initial numerical topology|Topology changes|Protected targets|Handoff|Gate 6|Gate 7|Gate 8|Gate 9|Gate 10" planning/BATTLE-SCENE-OA-TEMPLATE.md qa/BATTLE-SCENE-QA-STANDARD.md qa/QA-GATES.md
```

Expected: every required field appears in the template and the referenced standards; no field is named differently between the template and the audit plan.

- [ ] **Step 3: Commit the template**

```powershell
git add -- planning/BATTLE-SCENE-OA-TEMPLATE.md
git commit -m "docs: add battle scene OA template"
```

---

### Task 2: Create the Merrowgate battle/action audit and scene OA

**Files:**
- Create: `qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md`
- Reference: `volumes/VOLUME-002-MERROWGATE-ARCHITECTURE.md`, `chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md`, `planning/BATTLE-SCENE-OA-TEMPLATE.md`

**Interfaces:**
- Consumes: the template field names from Task 1 and the locked Merrowgate chapter architecture.
- Produces: battle/action IDs `V2-A01`, `V2-B01` through `V2-B06`, full encounter cards, and arc-level variety evidence used by Task 3 and Task 4.

- [ ] **Step 1: Add planning-only authority and scope**

Start the file with:

```markdown
# Volume 2 — Merrowgate Arc — Battle / Scene OA

**Project:** This Isekai Has a Bug. Unfortunately, It's Me.
**Volume:** 2 — Merrowgate Arc
**Destination:** DEST-002 — Merrowgate
**Status:** PLANNING MAP — NOT PROSE APPROVAL
**Standards:** `qa/BATTLE-SCENE-QA-STANDARD.md` + `qa/SCENE-QA-STANDARD.md`
**Roadmap:** `chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md`

This file assigns battle/action architecture only. It does not authorize manuscript prose, Gate 8 scene files, canonization, or publication changes.
```

- [ ] **Step 2: Add the arc composition map**

Add a table containing exactly these IDs and assignments:

| ID | Chapter | Classification | Matchup / action identity | Scale | Topology | Primary objective |
|---|---|---|---|---|---|---|
| V2-A01 | CH-033 | HAZARD ACTION | Red + workers vs warehouse/infrastructure emergency while cargo and injured people are protected | MINOR ACTION | split objective; hazard changes the available route | clear the immediate hazard and protect people/cargo |
| V2-B01 | CH-031 | BATTLE/ACTION | Red + Samir + shipwright crew vs shifting load/repair hazard | MINOR | uneven team vs one structural hazard; rescue/repair | complete the repair without making the yard less safe |
| V2-B02 | CH-036 | BATTLE/ACTION | Red + Samir + workers vs failing dry-dock system, water, and secondary collapse | MAJOR RESCUE | rescue under attack; split rescue points | extract trapped workers and prevent a second collapse |
| V2-B03 | CH-042 | BATTLE/ACTION | Red + Iria + Samir + dockworkers vs cargo-transfer failure and contested access/perimeter | MAJOR REVERSAL | multi-front rescue with public response opposed by private control | save people and stop cascade; the initial death cannot be undone |
| V2-B04 | CH-045 | BATTLE/ACTION | Red + Samir + trusted workers vs four private-security contractors | MINOR HOSTILE INTERCEPTION | 2v4 interception that becomes a Red 1v4 delay while the others withdraw | protect the inspection and avoid exposing the counter-plan |
| V2-B05 | CH-047 | BATTLE/ACTION | Harbor Watch, workers, and Red vs infrastructure/weather failures plus private-security seizure attempts | MAJOR / GREAT-BATTLE BUILD | multi-front defensive hold with reinforcement and route changes | keep public routes open and prevent private takeover |
| V2-B06 | CH-048 | BATTLE/ACTION | Split coalition fronts vs harbor failures, private security, and evidence seizure | CLIMAX | split-party/multi-front battle with changing objectives | preserve harbor function, secure evidence, and retain public command |
```

- [ ] **Step 3: Write the seven encounter cards**

For each ID, add the full template card. Use these locked decisions:

| ID | Protected targets | Red's role | Decisive non-Red roles | Topology change | Cost / handoff |
|---|---|---|---|---|---|
| V2-A01 | workers, injured people, active cargo | one bounded brace/obstruction utility only after workers establish the safe direction | workers clear people; Nessa/Dalen or site lead controls cargo priority | hazard shifts from one blocked lane to a secondary access problem | damaged cargo/time loss; CH-034/CH-035 pressure remains ordinary logistics, not combat escalation |
| V2-B01 | shipwrights and suspended load | follows Samir's load logic; any manifestation is support, not replacement | Samir owns load path and repair call; crew handles lines and footing | stable repair becomes emergency rescue/weight transfer | repair delay and increased cost; handoff to the port's real structural vulnerability |
| V2-B02 | trapped workers and dry-dock crews | enters the dangerous space for a bounded extraction support | Samir reads the structure; workers guide rescue; Iria controls access | one rescue point becomes two as water/secondary collapse changes the route | injuries, damage, and suspicion of non-random failure; handoff to pattern investigation |
| V2-B03 | dockworkers, civilians, adjacent platforms, evidence of the failure | rescues and supports one critical extraction without erasing the initial casualty or damage | Samir identifies altered mechanics; Iria commands perimeter/rescue; workers move people | rescue perimeter becomes contested access and public/private command conflict | one death, several injuries, infrastructure damage, Red's public suspect status; handoff to CH-043 |
| V2-B04 | inspection evidence, trusted workers, concealed countermeasures | delays/repositions or restrains only as needed; Red holds a temporary 1v4 delay rather than flattening four guards for spectacle | Samir preserves the inspection; workers create safe retreat; Nessa controls access timing | 2v4 interception becomes a Red 1v4 delay and split withdrawal with one route sacrificed to preserve the inspection | secrecy is partially compromised and the team loses time; handoff to CH-046 preparation |
| V2-B05 | workers, civilians, evacuation/cargo routes, public responders | performs exactly two sequential support manifestations at assigned points | Iria owns command; Samir owns structural response; Dalen owns movement; workers own physical execution | distributed failures become separate fronts; private security tries to seize one front | fatigue, damage, exposed priorities, and delayed evidence route; handoff to CH-048 |
| V2-B06 | harbor workers, evacuation lanes, records/evidence, public authority | chooses one intervention at a time and leaves other specialists their decisive scenes; exactly three sequential support manifestations | Nessa secures routes/evidence; Iria defeats private seizure legally/operationally; Samir holds the physical plan; Dalen keeps cargo/evacuation moving | split fronts converge only after evidence and public control survive the physical crisis | harbor survives with injury/death, infrastructure cost, political consequence, and Cassian's plan exposed; handoff to CH-049 |
```

- [ ] **Step 4: Add the topology and great-battle audits**

Document these conclusions with direct references to the encounter IDs:

- topology variety includes split-objective hazard action, uneven team versus structural hazard, rescue under attack, multi-front rescue, 2v4 hostile interception, defensive hold, split-party action, and changing objectives;
- CH-047→CH-048 is the great battle sequence;
- at least two non-Red characters own decisive actions in the great battle;
- CH-042, CH-047, and CH-048 have irreversible consequences;
- CH-031, CH-036, CH-042, CH-045, CH-047, and CH-048 each have a topology or objective change;
- CH-033 is action coverage but not a combat-topology count;
- defeating opponents is not the primary objective in CH-031, CH-036, CH-042, CH-045, CH-047, or CH-048.

- [ ] **Step 5: Add the explicit non-combat classification audit**

List `NO BATTLE` chapters exactly as:

```text
CH-027, CH-028, CH-029, CH-030, CH-032, CH-034, CH-035, CH-037, CH-038, CH-039, CH-040, CH-041, CH-043, CH-044, CH-046, CH-049, CH-050
```

State that these chapters retain social, investigative, legal, travel, or aftermath pressure without receiving a combat assignment. Keep CH-033 as `HAZARD ACTION` and keep the six `V2-B` entries as the battle/action assignments.

- [ ] **Step 6: Validate the audit fields**

Run:

```powershell
rg -n "V2-A01|V2-B01|V2-B02|V2-B03|V2-B04|V2-B05|V2-B06|Protected targets|Initial numerical topology|Topology changes|Terrain|Primary objective|Red's role|Decisive supporting|Turning point|Resolution|Cost|Handoff|NO BATTLE|great battle|2v4|1v4" qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md
```

Expected: all seven IDs and every required card field are present; `2v4` and `1v4` appear only in the private-security interception/great-battle topology discussion; the file states planning-only status.

- [ ] **Step 7: Commit the Merrowgate audit**

```powershell
git add -- qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md
git commit -m "docs: map Merrowgate battle and scene OA"
```

---

### Task 3: Connect OA assignments to the Merrowgate chapter roadmap

**Files:**
- Modify: `chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md`
- Reference: `qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md`

**Interfaces:**
- Consumes: the exact IDs/classifications from Task 2.
- Produces: chapter-level roadmap fields that tell Gate 7 and the future Gate 8 owner which battle/action structure is assigned.

- [ ] **Step 1: Add assignments to action chapters**

Add a `Battle / Scene OA` field adjacent to each chapter's existing `Action Progression` field:

```markdown
**Battle / Scene OA:** V2-B01 — BATTLE/ACTION; uneven team vs one structural hazard; repair objective changes into rescue/weight-transfer objective; detailed scene architecture deferred to Gate 8.
```

Use these exact assignments:

```text
CH-031 — V2-B01 — uneven team vs one structural hazard; rescue/repair objective.
CH-033 — V2-A01 — HAZARD ACTION; split objective; no combat-topology count.
CH-036 — V2-B02 — rescue under attack; split rescue points; trapped-worker objective.
CH-042 — V2-B03 — multi-front rescue; contested perimeter/access; casualty-prevention objective.
CH-045 — V2-B04 — natural 2v4 interception becoming a Red 1v4 delay; protect inspection/evidence objective.
CH-047 — V2-B05 — multi-front defensive hold; infrastructure/weather/private-security conflict.
CH-048 — V2-B06 — split-party/multi-front climax; evidence, evacuation, and public-command objectives.
```

- [ ] **Step 2: Mark non-combat chapters without rewriting their existing summaries**

Add `**Battle / Scene OA:** NO BATTLE — social/investigative/legal/travel/aftermath pressure only.` to the chapters listed in the audit's non-combat classification list. For CH-030 and CH-034/035, keep their existing work/suspense hazards classified as non-combat because the roadmap does not define a hostile action encounter.

- [ ] **Step 3: Add the roadmap cross-reference**

Immediately before the existing `# 8. Regeneration / Injury Continuity` heading, add:

```markdown
## Battle / Scene OA Cross-Reference

The arc-level matchup cards and topology audit are authoritative in:

`qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md`

This roadmap records Gate 7 assignments only. Detailed scene files are not created until the relevant chapter reaches Gate 8. The OA layer does not alter chapter order, climax placement, manifestation counts, injury continuity, mystery boundaries, or canon prose.
```

- [ ] **Step 4: Validate roadmap alignment**

Run:

```powershell
rg -n "V2-A01|V2-B01|V2-B02|V2-B03|V2-B04|V2-B05|V2-B06|Battle / Scene OA|NO BATTLE|Detailed scene files are not created" chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md
```

Expected: every ID appears in both files, each battle/action chapter has one assignment, every listed non-combat chapter has a `NO BATTLE` line, and the roadmap preserves the Gate 8 deferral.

- [ ] **Step 5: Commit the roadmap integration**

```powershell
git add -- chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md
git commit -m "docs: assign Merrowgate battle scene OA"
```

---

### Task 4: Run the cross-file and changed-scope verification

**Files:**
- Test: `planning/BATTLE-SCENE-OA-TEMPLATE.md`, `qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md`, `chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md`
- Reference: `docs/superpowers/specs/2026-09-20-battle-scene-oa-design.md`

**Interfaces:**
- Consumes: all artifacts from Tasks 1–3.
- Produces: evidence that the OA map is complete, internally consistent, and limited to the approved planning scope.

- [ ] **Step 1: Check formatting and unresolved markers**

Run:

```powershell
git diff --check
$files = @(
  'planning/BATTLE-SCENE-OA-TEMPLATE.md',
  'qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md',
  'chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md'
)
$markers = @('T'+'BD','T'+'ODO','FIX'+'ME','place'+'holder','implement'+' later')
$hits = Select-String -Path $files -Pattern $markers
if ($hits) { $hits | ForEach-Object { Write-Error $_ }; exit 1 }
```

Expected: `git diff --check` is silent and the unresolved-marker scan returns no matches.

- [ ] **Step 2: Check battle ID parity**

Run:

```powershell
$audit = Get-Content -Raw 'qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md'
$roadmap = Get-Content -Raw 'chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md'
foreach ($id in @('V2-A01','V2-B01','V2-B02','V2-B03','V2-B04','V2-B05','V2-B06')) {
  if ($audit -notmatch [regex]::Escape($id)) { throw "Missing $id from audit" }
  if ($roadmap -notmatch [regex]::Escape($id)) { throw "Missing $id from roadmap" }
}
Write-Output 'Battle/action ID parity: PASS'
```

Expected: `Battle/action ID parity: PASS`.

- [ ] **Step 3: Check non-combat exclusion and great-battle requirements**

Run:

```powershell
$audit = Get-Content -Raw 'qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md'
$roadmap = Get-Content -Raw 'chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md'
foreach ($chapter in @('CH-027','CH-028','CH-029','CH-030','CH-032','CH-034','CH-035','CH-037','CH-038','CH-039','CH-040','CH-041','CH-043','CH-044','CH-046','CH-049','CH-050')) {
  if ($audit -notmatch [regex]::Escape($chapter)) { throw "Non-combat chapter $chapter missing from audit" }
}
foreach ($required in @('CH-047','CH-048','2v4','multi-front','non-Red','not the primary objective','irreversible')) {
  if ($audit -notmatch [regex]::Escape($required)) { throw "Great-battle requirement missing: $required" }
}
Write-Output 'Non-combat and great-battle checks: PASS'
```

Expected: `Non-combat and great-battle checks: PASS`.

- [ ] **Step 4: Verify no manuscript or publication files changed**

Run:

```powershell
$baseline = git log --format='%H' --grep='docs: clarify hazard action coverage' -1
$changed = git diff "$baseline..HEAD" --name-only
$allowed = @(
  'docs/superpowers/plans/2026-09-20-battle-scene-oa-expansion.md',
  'planning/BATTLE-SCENE-OA-TEMPLATE.md',
  'qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md',
  'chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md'
)
$unexpected = $changed | Where-Object { $_ -notin $allowed }
if ($unexpected) { $unexpected | ForEach-Object { Write-Error "Unexpected changed file: $_" }; exit 1 }
if ($changed -match '^(manuscript|published)/') { throw 'Manuscript/publication files changed' }
Write-Output 'Changed-scope check: PASS'
```

Expected: `Changed-scope check: PASS`, with only the reviewed plan and three implementation artifacts listed. If the baseline commit message is unavailable, stop and compare against the implementation baseline before changing any user files.

- [ ] **Step 5: Commit verification evidence**

```powershell
git status --short
git log --oneline -4
```

Expected: a clean worktree and the three implementation commits after the two already-committed spec commits.

---

## Completion Checklist

- [ ] Template created and field names match the existing QA standards.
- [ ] Merrowgate audit created with `V2-A01` and `V2-B01` through `V2-B06`.
- [ ] CH-047→CH-048 documented as the great battle sequence.
- [ ] Natural 2v4/1v4 interception documented with objective-driven tactics.
- [ ] Non-Red decisive agency and non-defeat objectives documented.
- [ ] Non-combat chapters explicitly excluded from combat assignments.
- [ ] Roadmap IDs match audit IDs.
- [ ] No manuscripts or published copies changed.
- [ ] All verification commands pass.
