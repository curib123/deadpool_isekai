# Flexible Series Arc Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Add a quality-first flexible future-arc planning system that maps the story from the locked Merrowgate Arc toward the final arc without inventing a fixed arc count or prematurely canonizing later destinations.

**Architecture:** Create small authoritative planning and QA records for future arc functions, mystery windows, long-range consequences, battle topology, and endgame readiness. Synchronize the series roadmap and story-planning index to reference those records while preserving Gate 5–7 destination selection and the current CH-027 production priority. Validate the documentation with repeatable PowerShell assertions and a final cross-record QA report.

**Tech Stack:** Markdown canon/planning records, PowerShell read-only assertions, rg, Git.

**Spec:** docs/superpowers/specs/2026-09-20-flexible-series-arc-architecture-design.md

## Global Constraints

- The number of future arcs remains flexible; no artificial total is locked.
- Arc 1 / Greywake and Arc 2 / Merrowgate remain the only destination arcs with existing canon authority; later destinations remain unselected until Gate 5 passes.
- Every major volume uses one actual destination and is named [Destination Name] Arc.
- The future route is a story-function spine, not an open-ended travel anthology and not a fixed-volume outline.
- Red is already overwhelmingly powerful from the beginning; no conventional power-growth ladder, final form, or unlock-based progression may be introduced.
- Red's tension comes from information, judgment, restraint, access, reputation, consequences, and competing objectives rather than false power ceilings.
- The registered Hero, Hero Party, Main Villain, Fate, System, and Great Design remain independent and coherent; Red reroutes causality without replacing the native story.
- Future mystery scheduling may reference only authorized M-IDs/F-IDs and may not reveal protected writer truth ahead of the Mystery Bible's reveal windows.
- Every future arc must have distinct destination identity, local conflict, travel logic, supporting-cast autonomy, action geography, climax, aftermath, and departure consequence.
- Every future action-heavy arc requires at least one major battle, multiple appropriate minor action encounters, and varied topology when the local conflict naturally supports combat; no battle may exist only to increase quantity.
- Every future destination, volume, chapter, scene, manuscript, and publication copy remains provisional until its required studio gate passes.
- The immediate active production step remains CH-027 Soul-Drift/close-first-person synchronization and Gate 9 revalidation; this plan does not draft CH-027 or CH-028.
- Do not modify published/, create future manuscripts, create future scene architectures, or mark any future F-ID as planted in this implementation.

## Review Focus

- Future-slot language accidentally promoting a candidate destination or final stage into canon; test the registry and roadmap for LOCKED/CANON claims outside Greywake and Merrowgate.
- Mystery-window drift that treats a planned clue as planted or exposes protected M-001/M-003/M-004/M-006/M-008/M-009/M-010/M-012 truth early; test all M/F references and statuses against mysteries/MYSTERY-BIBLE.md.
- Consequence erasure or false Red progression; test that the ledger preserves current Greywake consequences, Merrowgate pending status, stable Red, and no power-tier language.
- Repetitive or power-ranking battle planning; test the topology ledger against the locked battle standard and require objective/terrain/consequence variation.
- Roadmap/index contradictions that authorize later production before Gate 5–7 or displace CH-027; test the final authority sections and link targets.

---

### Task 1: Create the flexible future-arc registry

**Files:**
- Create: planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md
- Read: docs/superpowers/specs/2026-09-20-flexible-series-arc-architecture-design.md
- Read: series/ROADMAP.md
- Read: destinations/DESTINATION-INVENTORY.md
- Read: qa/QA-GATES.md

**Interfaces:**
- Consumes: the five required story-function stages in the approved design and the current Greywake/Merrowgate authority in series/ROADMAP.md.
- Produces: the single registry that later planning tasks reference for future slot status, stage purpose, destination-selection state, admission criteria, merge/cut status, and next authorized production step.

- [ ] **Step 1: Define the registry status vocabulary before writing rows.**

Use exactly these meanings in the document:

~~~text
LOCKED     — approved destination/volume architecture exists at its owning gate.
CANON      — manuscript and continuity are current at the applicable canon gate.
IN-PRODUCTION — the locked destination is actively being produced under its gate sequence.
PROVISIONAL — a story-function slot exists, but no destination or volume is canon.
MERGED     — the function was absorbed into another approved arc; no independent arc exists.
CUT        — the function was removed because the stop/merge tests failed.
UNSELECTED — no destination has passed Gate 5 for this function.
~~~

- [ ] **Step 2: Add the authority table for existing arcs.**

Record:

| Record | Destination | State | Authority | Next action |
|---|---|---|---|---|
| ARC-001 | DEST-001 Greywake | CANON / RELEASE-READY | Volume 1 destination, 26-chapter canon, Gate 10 and Gate 11 records | No new Arc 1 prose unless explicitly reopened |
| ARC-002 | DEST-002 Merrowgate | LOCKED / IN-PRODUCTION | Volume 2 architecture and CH-027–CH-050 roadmap | CH-027 synchronization → Gate 9 |

Do not rewrite Arc 2's chapter content or claim CH-027 is current if the latest synchronization authority still marks its prose stale.

- [ ] **Step 3: Add the five provisional story-function slots without destinations.**

Use these slot IDs and functions:

| Slot | Function | Mystery window | Destination state | Arc state |
|---|---|---|---|---|
| SLOT-A | Identity and Registration Pressure | M-002, M-011; later F-011 when authorized | UNSELECTED | PROVISIONAL |
| SLOT-B | Body and Anomaly Consequences | M-004, M-005, M-006; F-018 only in its approved crisis window | UNSELECTED | PROVISIONAL |
| SLOT-C | Ancient History and Boundary Evidence | M-009; F-007/F-008/F-009/F-014 as separately scheduled | UNSELECTED | PROVISIONAL |
| SLOT-D | Exploitation and Savael | M-001, M-010; F-015/F-016 as separately scheduled | UNSELECTED | PROVISIONAL |
| SLOT-E | Fate, Great Design, and Endgame Choice | M-007, M-008, M-012; F-017/F-019/F-020 | UNSELECTED | PROVISIONAL |

The rows must explicitly state that adjacent slots may be combined only after Gate 5/6 proves the destination can carry both functions without compressing the reveal ladder.

- [ ] **Step 4: Add admission, merge, cut, and final-arc readiness columns.**

Each provisional row must answer:

~~~text
Required before admission: unresolved story job, eligible destination, distinct local conflict, mystery-safe advancement, Red reroute, distinct action/aftermath profile.
Merge test: same local conflict, same mystery function, or removable without damaging the endgame spine.
Cut test: no unique consequence, no destination identity, repeated climax, or resolved before planned ending.
Final-arc test: protected mysteries ready, native story resolution ready, structural choice supported, destination conflict and aftermath ready.
~~~

- [ ] **Step 5: Run registry assertions before committing.**

Run:

~~~powershell
$p = 'planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md'
$t = Get-Content -Raw $p
if ($t -notmatch 'ARC-001.*Greywake' -or $t -notmatch 'ARC-002.*Merrowgate') { throw 'Existing arc authority rows missing' }
if ($t -notmatch 'SLOT-A' -or $t -notmatch 'SLOT-E') { throw 'All future story-function slots are required' }
if ($t -match 'Volume 3.*LOCKED|DEST-00[3-9].*CANON|Final Destination.*LOCKED') { throw 'Future destination was prematurely canonized' }
if ($t -notmatch 'Gate 5' -or $t -notmatch 'Gate 6' -or $t -notmatch 'Gate 7') { throw 'Destination and production gates are missing' }
~~~

- [ ] **Step 6: Commit the registry.**

~~~powershell
git add planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m "planning: add flexible future arc registry"
~~~

### Task 2: Create the future mystery-window schedule

**Files:**
- Create: planning/FUTURE-MYSTERY-WINDOW-SCHEDULE.md
- Read: mysteries/MYSTERY-BIBLE.md
- Read: continuity/MYSTERY-KNOWLEDGE-STATE.md
- Read: planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md
- Read: qa/MYSTERY-FOUNDATION-QA.md

**Interfaces:**
- Consumes: future slot IDs from Task 1 and authoritative M/F definitions from the Mystery Bible.
- Produces: the schedule that identifies allowed mystery movement, planned-but-unplanted clues, forbidden early reveals, and the knowledge-state handoff each future slot must provide.

- [ ] **Step 1: Create the schedule header and status rule.**

State that this record schedules reveal windows only; it cannot plant an F-ID, alter writer truth, or make a future destination canon. Use these statuses:

~~~text
CURRENT / PLANTED       — only when an existing canon manuscript and QA record prove it.
PLANNED / NOT PLANTED   — authorized future setup with no manuscript evidence yet.
PROTECTED               — writer truth or reveal boundary cannot be advanced in this slot.
DEFERRED                — the clue may be revisited only after a later gate.
~~~

- [ ] **Step 2: Record the already-canon Arc 1 and Arc 2 boundaries.**

Use the current repository records to state:

- F-001, F-002, F-003, and F-004 are planted in Arc 1 at their existing chapter locations.
- F-010 is planned for CH-038 in Merrowgate and remains PLANNED / NOT PLANTED until manuscript evidence and Gate 9 pass.
- M-002 has surface reinforcement only; M-001, M-003, M-004 writer truth, M-006 metaphysics, M-008, M-009 full history, M-010, M-011 deep truth, and M-012 remain protected according to current authority.

- [ ] **Step 3: Add the stage schedule.**

For each SLOT-A through SLOT-E, include:

~~~text
Allowed M-IDs:
Allowed F-IDs:
Required reader-facing change:
Writer truth still protected:
False beliefs that may grow:
Knowledge-state handoff to the next slot:
Disallowed shortcut:
~~~

The final slot must not mark M-012 resolved. It may mark the final choice as READY ONLY AFTER the prerequisites are proven.

- [ ] **Step 4: Cross-check every referenced ID against the Mystery Bible.**

Run:

~~~powershell
$m = Get-Content -Raw 'mysteries/MYSTERY-BIBLE.md'
$s = Get-Content -Raw 'planning/FUTURE-MYSTERY-WINDOW-SCHEDULE.md'
$ids = [regex]::Matches($s, '\b(?:M|F)-\d{3}\b') | ForEach-Object Value | Sort-Object -Unique
foreach ($id in $ids) { if ($m -notmatch [regex]::Escape($id)) { throw "Unknown mystery ID: $id" } }
if ($s -match 'M-012.*(?:RESOLVED|ANSWERED|PAID OFF)' -and $s -notmatch 'FINAL CHOICE.*READY ONLY AFTER') { throw 'M-012 was resolved too early' }
if ($s -match 'F-010.*PLANTED' -and $s -notmatch 'F-010.*NOT PLANTED') { throw 'F-010 status drifted' }
~~~

- [ ] **Step 5: Commit the schedule.**

~~~powershell
git add planning/FUTURE-MYSTERY-WINDOW-SCHEDULE.md
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m "planning: schedule future mystery windows"
~~~

### Task 3: Create the long-range consequence and native-story ledger

**Files:**
- Create: continuity/SERIES-CONSEQUENCE-LEDGER.md
- Read: continuity/CONTINUITY-BIBLE.md
- Read: continuity/MYSTERY-KNOWLEDGE-STATE.md
- Read: series/NATIVE-STORY-FRAMEWORK.md
- Read: characters/CHARACTER-BIBLE.md
- Read: volumes/VOLUME-001-GREYWAKE-ARCHITECTURE.md
- Read: volumes/VOLUME-002-MERROWGATE-ARCHITECTURE.md
- Read: chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md

**Interfaces:**
- Consumes: current continuity rules, Arc 1 canon, Arc 2 planned consequences, and future slot IDs.
- Produces: the cross-arc state ledger for Red, the native Hero/Party, Savael, institutions/factions, destination condition, travel, injuries/resources, reputation, relationships, and unresolved conflicts.

- [ ] **Step 1: Define state labels and actor columns.**

Use these state labels:

~~~text
CANON       — supported by current manuscript/canon records.
PLANNED     — authorized by a locked roadmap but not yet manuscript canon.
PROVISIONAL — story-function expectation only.
PROTECTED   — must not be advanced by this record.
UNRESOLVED  — deliberately open and carried forward.
~~~

Every arc/stage row must have these columns:

~~~text
Route record | State | Red location/condition | Red injuries/resources | Red reputation/relationships | Native Hero/Party state | Savael state | Institution/faction changes | Destination condition | Active mysteries/clues | Travel/departure consequence | Next handoff
~~~

- [ ] **Step 2: Record Arc 1's canon baseline without inventing new prose.**

Record only consequences supported by existing authority: Greywake survives with damage and political/institutional consequences; Red departs as an undefined outsider whose reputation has changed; existing injury/recovery, F-ID plant, local-faction, and travel states remain linked to their owning records; Red's power does not progress.

- [ ] **Step 3: Record Arc 2 as planned/in production, not completed future canon.**

Use the Merrowgate architecture/roadmap to record the planned arrival, commercial/security conflict, Cassian Venn pressure, local cast responsibilities, CH-042 casualty/reversal, CH-047/048 climax shape, CH-049 resolution, CH-050 departure, and the rule that these remain PLANNED until chapter manuscript and Gate 9/10 records prove them. Keep CH-027's current synchronization status unchanged.

- [ ] **Step 4: Add provisional rows for SLOT-A through SLOT-E.**

Each row must show an unresolved handoff rather than a fabricated event. Include the expected consequence class:

- SLOT-A: a practical identity/registration workaround or institutional consequence;
- SLOT-B: an anomaly-related cost or misinterpretation without a power tier;
- SLOT-C: historical evidence that changes faction behavior and route pressure;
- SLOT-D: exploitation pressure that forces Red to reject or redirect an imposed role;
- SLOT-E: a structural choice whose consequences affect Veyr and Red without conventional Hero conversion.

- [ ] **Step 5: Run consequence assertions.**

~~~powershell
$p = Get-Content -Raw 'continuity/SERIES-CONSEQUENCE-LEDGER.md'
foreach ($needle in @('Red Jackal','Native Hero','Hero Party','Savael','Destination condition','Travel/departure consequence')) { if ($p -notmatch [regex]::Escape($needle)) { throw "Missing ledger column/content: $needle" } }
if ($p -match 'Red.*Stage [IVX]+|power progression|final form|level up') { throw 'Forbidden Red progression language found' }
if ($p -notmatch 'Merrowgate.*PLANNED|PLANNED.*Merrowgate') { throw 'Merrowgate planned state missing' }
~~~

- [ ] **Step 6: Commit the consequence ledger.**

~~~powershell
git add continuity/SERIES-CONSEQUENCE-LEDGER.md
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m "continuity: add series consequence ledger"
~~~

### Task 4: Create the battle-topology ledger

**Files:**
- Create: planning/BATTLE-TOPOLOGY-LEDGER.md
- Read: qa/BATTLE-SCENE-QA-STANDARD.md
- Read: planning/BATTLE-SCENE-OA-TEMPLATE.md
- Read: qa/VOLUME-001-GREYWAKE-BATTLE-SCENE-AUDIT.md
- Read: qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md
- Read: chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md
- Read: planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md

**Interfaces:**
- Consumes: existing Arc 1/Arc 2 battle audits and future slot IDs.
- Produces: a series-wide topology ledger that prevents repetitive action design and keeps future battle plans provisional until their arc/chapter gates pass.

- [ ] **Step 1: Define the topology vocabulary and required matchup fields.**

Use the locked Battle Scene QA Standard's topologies: 1v1, 2v1, 1v2, 1v4/1vMany, 2v2, uneven team, rotating opponents, split-party, escort, defensive hold, pursuit/interception, rescue under attack, three-sided conflict, environmental action, and multi-front action.

Every major entry must also identify objective, terrain, information asymmetry, Red's chosen role, supporting-character ownership, why immediate overwhelming force is not the objective, turning point, immediate cost, lasting consequence, and next-scene handoff.

- [ ] **Step 2: Record verified Arc 1 and planned Arc 2 references.**

Do not duplicate or contradict the detailed audit. Link to the existing Greywake battle audit for verified variety. Link to the Merrowgate roadmap/audit for V2-B01 through V2-B06 and label those entries PLANNED until their scene/manuscript gates pass.

- [ ] **Step 3: Add future slot action requirements without inventing battles.**

For SLOT-A through SLOT-E, record only topology targets and action-purpose requirements:

~~~text
At least one major/great battle where the local conflict supports combat.
At least two minor action encounters when natural to the destination.
At least three distinct topologies across a longer battle-capable arc.
At least one scene where Red is not the only decisive actor.
At least one scene whose primary objective is not defeating the enemy.
At least one terrain/civilian/evidence/infrastructure/timing complication.
~~~

State that exact matchups are deferred to Gate 6/7 and detailed Battle/Scene OA is deferred to Gate 8.

- [ ] **Step 4: Run topology assertions.**

~~~powershell
$p = Get-Content -Raw 'planning/BATTLE-TOPOLOGY-LEDGER.md'
foreach ($needle in @('1v1','2v1','1v4','defensive hold','multi-front','terrain','supporting-character')) { if ($p -notmatch [regex]::Escape($needle)) { throw "Missing battle-topology requirement: $needle" } }
if ($p -match 'SLOT-[A-E].*(?:CANON|PUBLISH-READY|finalized matchup)') { throw 'Future battle was prematurely canonized' }
if ($p -notmatch 'not defeating the enemy') { throw 'Objective-based action requirement missing' }
~~~

- [ ] **Step 5: Commit the topology ledger.**

~~~powershell
git add planning/BATTLE-TOPOLOGY-LEDGER.md
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m "planning: add flexible battle topology ledger"
~~~

### Task 5: Create the endgame readiness and stop-condition QA record

**Files:**
- Create: qa/FLEXIBLE-ARC-ENDGAME-READINESS.md
- Read: mysteries/MYSTERY-BIBLE.md
- Read: qa/QA-GATES.md
- Read: qa/PUBLISH-VERSION-QA-STANDARD.md
- Read: planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md
- Read: planning/FUTURE-MYSTERY-WINDOW-SCHEDULE.md
- Read: continuity/SERIES-CONSEQUENCE-LEDGER.md
- Read: planning/BATTLE-TOPOLOGY-LEDGER.md

**Interfaces:**
- Consumes: all four series-level records created by Tasks 1–4.
- Produces: the review board's current verdict on whether a future slot, the final arc, or the series ending is ready to advance.

- [ ] **Step 1: Add the current verdict.**

Set:

~~~text
Flexible future route: ACTIVE / PROVISIONAL
Arc 1: COMPLETE / RELEASE-READY
Arc 2: LOCKED / IN PRODUCTION
Future destinations: NOT SELECTED
Final arc: NOT READY
Series stop condition: NOT YET SATISFIED
Immediate production authorization: CH-027 synchronization → Gate 9
~~~

- [ ] **Step 2: Add the arc-admission checklist.**

Require all of the following before a future slot becomes a destination arc: existing eligible place, Gate 5 selection, distinct culture, local conflict, travel entry/exit, mystery-safe window, supporting-cast autonomy, Battle Composition Map where applicable, Gate 6 volume architecture, Gate 7 chapter roadmap, and no unresolved higher-level contradiction.

- [ ] **Step 3: Add the merge/cut checklist.**

Require a documented merge or cut decision when a candidate repeats a local conflict, duplicates a mystery function, has no distinct aftermath, resolves before its planned ending, or can be removed without damaging the story spine.

- [ ] **Step 4: Add the final-arc readiness checklist.**

Mark a final arc ready only when M-001 through M-012 have authorized payoffs, protected F-IDs have planted/payoff records, native-story resolution is independently viable, the structural choice is supported, the final destination passes Gate 5, the local conflict and aftermath are designed, and no extra explanatory arc is required.

- [ ] **Step 5: Run readiness assertions.**

~~~powershell
$p = Get-Content -Raw 'qa/FLEXIBLE-ARC-ENDGAME-READINESS.md'
foreach ($needle in @('Final arc: NOT READY','Future destinations: NOT SELECTED','CH-027 synchronization','Gate 5','Gate 6','Gate 7','Gate 9','Gate 10','Gate 11')) { if ($p -notmatch [regex]::Escape($needle)) { throw "Readiness state missing: $needle" } }
if ($p -match 'Final arc: READY|Series stop condition: SATISFIED') { throw 'Series was incorrectly declared finished' }
~~~

- [ ] **Step 6: Commit the readiness QA record.**

~~~powershell
git add qa/FLEXIBLE-ARC-ENDGAME-READINESS.md
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m "qa: add flexible arc endgame readiness gate"
~~~

### Task 6: Synchronize the authoritative roadmap and planning index

**Files:**
- Modify: series/ROADMAP.md
- Modify: planning/STORY-PLANNING.md
- Modify: continuity/CONTINUITY-BIBLE.md
- Read: studio/STUDIO-ARCHITECTURE.md
- Read: series/SERIES-CONSTITUTION.md
- Read: docs/superpowers/specs/2026-09-20-flexible-series-arc-architecture-design.md
- Read: planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md
- Read: qa/FLEXIBLE-ARC-ENDGAME-READINESS.md

**Interfaces:**
- Consumes: the new registry, readiness record, and approved design specification.
- Produces: discoverable authority links and unambiguous roadmap language without changing Arc 1 canon, Arc 2 chapter content, CH-027 synchronization status, or future destination selection state.

- [ ] **Step 1: Add a latest-authority section to series/ROADMAP.md.**

Place it after the current synchronization authority so it is visibly later than historical statements. State:

~~~text
Flexible Future Arc Architecture: ACTIVE / QUALITY-FIRST / VARIABLE ARC COUNT
Registry: planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md
Mystery windows: planning/FUTURE-MYSTERY-WINDOW-SCHEDULE.md
Consequence ledger: continuity/SERIES-CONSEQUENCE-LEDGER.md
Battle topology ledger: planning/BATTLE-TOPOLOGY-LEDGER.md
Endgame readiness: qa/FLEXIBLE-ARC-ENDGAME-READINESS.md
Future destinations: no Volume 3+ destination is selected or canon.
Immediate next step: CH-027 rewrite/revalidation → Gate 9.
~~~

Keep the existing no-fixed-destination-order and Volume 3 selection-deferred rules. Do not replace historical records; make the latest authority explicit.

- [ ] **Step 2: Add a future-planning section to planning/STORY-PLANNING.md.**

Link the five records and state that future work proceeds by Destination Selection Gate 5 → Volume/Arc Gate 6 → Chapter Gate 7 → Scene Gate 8 → Manuscript Gate 9 → Canon Gate 10 → Publish Gate 11, with exact destination selection deferred until Gate 5.

- [ ] **Step 3: Add a continuity index entry.**

In continuity/CONTINUITY-BIBLE.md, link continuity/SERIES-CONSEQUENCE-LEDGER.md as the series-scale supplement to the chapter/volume ledger. State that the supplement cannot override a current manuscript, knowledge-state record, or higher canon Bible.

- [ ] **Step 4: Run synchronization assertions.**

~~~powershell
$files = @('series/ROADMAP.md','planning/STORY-PLANNING.md','continuity/CONTINUITY-BIBLE.md')
foreach ($f in $files) { if (-not (Test-Path $f)) { throw "Missing index file: $f" } }
$r = Get-Content -Raw 'series/ROADMAP.md'
$p = Get-Content -Raw 'planning/STORY-PLANNING.md'
foreach ($needle in @('FLEXIBLE-FUTURE-ARC-REGISTRY.md','FUTURE-MYSTERY-WINDOW-SCHEDULE.md','SERIES-CONSEQUENCE-LEDGER.md','BATTLE-TOPOLOGY-LEDGER.md','FLEXIBLE-ARC-ENDGAME-READINESS.md')) { if ($r -notmatch [regex]::Escape($needle) -and $p -notmatch [regex]::Escape($needle)) { throw "New authority not indexed: $needle" } }
if ($r -notmatch 'CH-027.*Gate 9' -and $r -notmatch 'Gate 9.*CH-027') { throw 'Current CH-027 production priority disappeared' }
if ($r -match 'Volume 3.*(?:CANON|LOCKED|PUBLISH-READY)') { throw 'Roadmap prematurely locked a future volume' }
~~~

- [ ] **Step 5: Commit the synchronization.**

~~~powershell
git add series/ROADMAP.md planning/STORY-PLANNING.md continuity/CONTINUITY-BIBLE.md
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m "roadmap: synchronize flexible future arc authority"
~~~

### Task 7: Run aggregate flexible-architecture QA and handoff

**Files:**
- Create: qa/FLEXIBLE-ARC-ARCHITECTURE-QA.md
- Read: all files created or modified in Tasks 1–6
- Read: studio/STUDIO-ARCHITECTURE.md
- Read: qa/QA-GATES.md
- Read: qa/BATTLE-SCENE-QA-STANDARD.md
- Read: qa/PUBLISH-VERSION-QA-STANDARD.md

**Interfaces:**
- Consumes: the complete flexible-arc record set and the locked studio standards.
- Produces: an evidence-backed aggregate QA verdict and explicit next-step authorization boundary.

- [ ] **Step 1: Write the aggregate checklist with one row per requirement.**

The QA record must cover:

~~~text
Flexible count, no filler rule, story-function stages, Gate 5–7 destination protection, Mystery Bible cross-reference, F-ID status, Red stable-power rule, native Hero/Party independence, consequence handoff, battle variety, Battle/Scene OA deferral, merge/cut rules, final-arc readiness, roadmap links, no publication changes, and CH-027 next-step preservation.
~~~

Every row must include Requirement, Evidence, Result, and Owner using studio agent IDs from studio/STUDIO-ARCHITECTURE.md.

- [ ] **Step 2: Run the full read-only QA command set.**

~~~powershell
git diff --check
$required = @(
  'planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md',
  'planning/FUTURE-MYSTERY-WINDOW-SCHEDULE.md',
  'continuity/SERIES-CONSEQUENCE-LEDGER.md',
  'planning/BATTLE-TOPOLOGY-LEDGER.md',
  'qa/FLEXIBLE-ARC-ENDGAME-READINESS.md',
  'qa/FLEXIBLE-ARC-ARCHITECTURE-QA.md'
)
foreach ($f in $required) { if (-not (Test-Path $f)) { throw "Missing required record: $f" } }
$all = ($required | ForEach-Object { Get-Content -Raw $_ }) -join [Environment]::NewLine
$badWords = @('T' + 'BD','TO' + 'DO','fill ' + 'in','implement ' + 'later')
foreach ($badWord in $badWords) { if ($all -match [regex]::Escape($badWord)) { throw 'Placeholder language remains' } }
if ($all -match 'Volume 3.*(?:CANON|LOCKED|PUBLISH-READY)') { throw 'Future volume is prematurely authoritative' }
if ($all -match 'M-012.*(?:RESOLVED|ANSWERED|PAID OFF)') { throw 'Endgame mystery was prematurely resolved' }
if ($all -match 'Red.*(?:Stage IV|final form|level up|power progression)') { throw 'Forbidden power progression remains' }
git status --short
~~~

Expected result: all assertions pass; only the intended documentation changes are present; no manuscript or publication files are modified.

- [ ] **Step 3: Record the verdict and exact next authorization.**

The final record must state FLEXIBLE ARC ARCHITECTURE QA: PASS only if all Task 1–6 assertions pass. It must state that the next authorized story-production step is CH-027 synchronization/Gate 9 and that no future destination-selection or later manuscript work is authorized by this architecture alone.

- [ ] **Step 4: Commit the aggregate QA record.**

~~~powershell
git add qa/FLEXIBLE-ARC-ARCHITECTURE-QA.md
git -c user.name='John Paul Cajes Curib' -c user.email='109894757+curib123@users.noreply.github.com' commit -m "qa: validate flexible series arc architecture"
~~~

- [ ] **Step 5: Final handoff verification.**

Run:

~~~powershell
git log --oneline -8
git status --short --branch
git diff master...HEAD --name-only
~~~

Expected result: the branch contains only the approved flexible-architecture records, roadmap/index synchronization, and QA documentation; manuscript/, published/, and future destination/volume/chapter files are absent from the changed-file list.

## Completion Contract

The implementation is complete only when:

- the flexible registry distinguishes locked canon from provisional story-function slots;
- the mystery schedule preserves planted/planned/protected states;
- the consequence ledger carries Red, native-story, Savael, institutional, destination, travel, and unresolved states;
- the topology ledger preserves battle variation without inventing future matchups;
- the endgame readiness record says the final arc is not ready until its prerequisites pass;
- roadmap and planning indexes point to every authoritative record;
- aggregate QA passes with no placeholders, no premature destination canon, no premature M-012 resolution, and no forbidden Red progression;
- Arc 1 remains release-ready, Arc 2 remains locked/in production, CH-027 remains the immediate next production step, and no manuscript/publication copy is changed by this implementation.
