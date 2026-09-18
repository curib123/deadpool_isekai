# Red Jackal Phase 1 Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and QA the complete macro world for the Red Jackal light novel without creating any arc, chapter, scene, or manuscript content.

**Architecture:** Keep `world/WORLD-BIBLE.md` authoritative for physical, political, cultural, historical, economic, travel, faction, and ecological canon. Keep `systems/SYSTEMS-BIBLE.md` authoritative for metaphysical and power-system rules. Record evidence in `qa/FOUNDATION-QA.md`, and change `series/ROADMAP.md` only from blocked to eligible while leaving its route table empty.

**Tech Stack:** Markdown canon documents, PowerShell content checks, Git commits.

**Spec:** `docs/superpowers/specs/2026-09-18-red-jackal-phase-1-foundation-design.md`

## Global Constraints

- World first. Destination second. Story third.
- Do not create arcs, chapters, scenes, manuscript prose, or a destination order in this phase.
- Preserve the locked Red Jackal status: `UNDEFINED` fields, `NO RECORD` registries, `FAILED` recognition, and `ANOMALY` classification.
- Keep the World System, magic, reincarnation, Fate, Great Design, Red Jackal anomaly, and Play Logic distinct.
- Make geography explain climate, settlement, borders, trade, and danger.
- Make cultures non-interchangeable after names are removed.
- Keep the Great Design's deepest truth writer-only and bounded.
- Commit each completed task separately with a specific message.

---

### Task 1: Build the authoritative macro World Bible

**Files:**
- Modify: `world/WORLD-BIBLE.md`

**Interfaces:**
- Consumes: `series/SERIES-CONSTITUTION.md`, `studio/STUDIO-ARCHITECTURE.md`, and the approved Phase 1 design.
- Produces: named world IDs and cross-references consumed by the Systems Bible and Foundation QA.

- [ ] **Step 1: Replace the empty world identity template with the named macro setting.**

Define the world as **Veyr**, a materially spherical world within a larger multiversal boundary called the Closed Loom. Establish the known inner hemisphere, the unmapped outer hemisphere, the polar regions, divine and demonic territories, the Ashfall Belt anomaly zone, and the Night Seam dimensional boundary. State that the System's known map is incomplete rather than treating the world as small.

- [ ] **Step 2: Add a geography registry with connected landforms.**

Create entries for:

- `CONTINENT-01` **Avarra**, the central temperate continent shaped by the Crownspine Mountains and the Sable River.
- `CONTINENT-02` **Kharad**, the southern dry continent separated by the Brasswater Sea and organized around salt basins and monsoon coasts.
- `CONTINENT-03` **Namarra**, the eastern rain continent beyond the Glass Current, with cloud forests and the living rootlands.
- `CONTINENT-04` **The Outer Pale**, the northern polar/fringe continent with glacial shelves and unreliable map geometry.
- `SEA-01` **Brasswater Sea**, `SEA-02` **Glass Current**, and `SEA-03` **The Widow's Reach**, each with currents, weather, ports, routes, monsters, and supernatural behavior.
- `ISLAND-01` **Morrowchain**, `ISLAND-02` **Lantern Atoll**, and `ISLAND-03` **The Unmoored Isle**, each with population/government/culture and a reason to remain unused as a future destination.
- Major regions, places, and landmarks including **Crownspine**, **Sable Basin**, **Red Fen**, **Hollow March**, **Ilyr Gate**, **Veyrhold**, **Salt-King's Stair**, **Lumenfall**, and **The Bell Under Snow**.

For each entry explain why the physical feature exists, how it affects routes and settlement, and which later fields depend on it.

- [ ] **Step 3: Add nations and political pressures.**

Define at least five major states with different institutions:

- `NATION-01` **The Kingdom of Valedorn**, elective crown and river nobility.
- `NATION-02` **The Serekh League**, council of chartered oasis cities.
- `NATION-03` **The Tazuun Dominion**, hereditary imperial provinces tied to irrigation and cavalry.
- `NATION-04` **The Rootbound Concord**, federated forest communities with rotating speaker houses.
- `NATION-05` **The Pale Marches**, fortress communes governed by seasonal military assemblies.

Give each state leadership, succession, peoples, language, religion, currency, magic level, military, economy, resources, borders, allies/enemies, factions, laws, history, System relationship, and current political problem. Include smaller polities and disputed corridors so borders do not become flat color blocks.

- [ ] **Step 4: Add differentiated cultures and factions.**

Define at least five cultures, with their own values, family structures, social hierarchy, clothing, food, architecture, etiquette, festivals, marriage, funerals, art/music, naming, taboos, religion, magic traditions, and historical trauma. Make the Valedorn river culture, Serekh caravan culture, Tazuun basin culture, Rootbound grove culture, and Pale March survival culture visibly and behaviorally distinct.

Add macro factions such as the **Ledger of Measures**, **Ash Choir**, **Open Hand Caravans**, **Crownspine Wardens**, and **Daughters of the Last Bell**, including public purpose, true agenda, resources, allies, enemies, hidden knowledge, and Red Jackal relationship.

- [ ] **Step 5: Add original history and knowledge layers.**

Create an era sequence from the First Weathering through the River Crowns, Salt Schism, Root War, Quiet Registration, and present **Year 612 of the Concord Calendar**. Each historical entry must include cause, participants, immediate/long-term consequences, public version, false version, hidden truth, and links to System/Fate/Great Design. Add a compact knowledge-layer table for the world's major unresolved truths.

- [ ] **Step 6: Add economy, travel, ecology, and future capacity.**

Define the crown, mark, salt-weight, and lumen currencies; explain exchange and debasement. Give travel times for roads, caravans, ships, passes, and licensed gates; define border controls, checkpoints, guild fees, and teleportation limits. Add creature entries for ordinary, magical, and anomaly-linked species whose ranges and food webs follow the geography. End with a registry of at least twelve unused destination candidates, explicitly marked as place records rather than arcs.

- [ ] **Step 7: Review for source-of-truth integrity and commit.**

Search the file for empty template labels, unresolved fields, accidental arc/chapter content, and contradictions with the locked constitution. Run `git diff --check`, inspect the full diff, and commit:

```powershell
git add world/WORLD-BIBLE.md
git commit -m "world: build phase 1 macro setting"
```

---

### Task 2: Build the authoritative Systems Bible

**Files:**
- Modify: `systems/SYSTEMS-BIBLE.md`

**Interfaces:**
- Consumes: the World Bible IDs and the locked Red Jackal status from the Series Constitution.
- Produces: explicit rules and limits consumed by Foundation QA and all later character/destination work.

- [ ] **Step 1: Define the World System as a bounded registry.**

Specify the System's origin as a later regulatory layer, its jurisdiction, registration lifecycle, normal fields, leveling, classes, attributes, skills, titles, blessings, curses, racial differences, class advancement, death handling, and interaction with magic and Fate. Explain what the System cannot observe or rewrite.

- [ ] **Step 2: Define magic independently from System permission.**

Establish mana sources, training, casting, spell creation, exhaustion, failure, artifacts, schools, regional traditions, divine/demonic/ancient variants, social access, and how System registration may describe but not create magic. Include at least four regional traditions corresponding to the World Bible cultures.

- [ ] **Step 3: Define reincarnation, Fate, and Great Design as separate authorities.**

Document normal soul origin, death, afterlife, reincarnation frequency, memory retention, soul registry, cross-world souls, forbidden experiments, and known anomalies. Define Fate's probability/convergence authority and limits. Define the Great Design's writer truth, purpose, scope, correction behavior, relationship to gods/System/Fate, and strict reveal boundary.

- [ ] **Step 4: Preserve and expand the Red Jackal anomaly.**

Retain every locked field and terminology rule from the existing Systems Bible. Add observable symptoms, what ordinary people and experts infer, what the System reports, what Red Jackal can learn, and what he cannot bypass. Explicitly prohibit hidden normal levels, conventional hidden classes, secret XP, or automatic immunity.

- [ ] **Step 5: Define Play Logic with progression and counterplay.**

Describe imagination-based expressions, mastery stages, interpretation errors, focus, scale, duration, material/symbolic complexity, collateral, recovery, world-law resistance, Fate interference, System interference, sealing, soul damage, causality/conceptual attacks, and existence-targeting threats. Provide examples of low-, mid-, and high-mastery effects without turning them into plot scenes or chapter events.

- [ ] **Step 6: Review the rule boundaries and commit.**

Check that no system is described as omnipotent, no Red Jackal field is normalized, and no arc/chapter content has been introduced. Run `git diff --check`, inspect the full diff, and commit:

```powershell
git add systems/SYSTEMS-BIBLE.md
git commit -m "systems: establish phase 1 world rules"
```

---

### Task 3: Record Foundation QA and unlock only the next planning gate

**Files:**
- Create: `qa/FOUNDATION-QA.md`
- Modify: `series/ROADMAP.md`

**Interfaces:**
- Consumes: the completed World Bible and Systems Bible.
- Produces: a dated QA decision and a roadmap gate state with no route entries.

- [ ] **Step 1: Create the QA evidence record.**

Record owners, review date, reviewed files, and a PASS/FAIL checklist for continents, seas, islands/regions, nations, cultures, history, economy/travel, ecology, reincarnation, World System, magic, Fate, Great Design, anomaly, Play Logic, unused places, and scope control. For every passed item cite the relevant section or ID. Record any non-blocking future-detail boundary without calling it missing foundation.

- [ ] **Step 2: Verify no story planning slipped into Phase 1.**

Use PowerShell checks against `world/`, `systems/`, and `series/ROADMAP.md` to confirm there are no destination-order rows, arc labels, chapter sheets, scene sheets, or manuscript additions. Place records may exist only as unused world geography.

- [ ] **Step 3: Update the roadmap gate without adding arcs.**

Change the roadmap status to `ELIGIBLE FOR DESTINATION SELECTION AFTER FOUNDATION QA`, keep the destination table header empty, and state that Phase 2 character work and later destination planning remain separate decisions.

- [ ] **Step 4: Run the full content QA and commit.**

Run the repository checks below, inspect `git diff --check`, and commit:

```powershell
rg -n "TODO|TBD|Name;|Define |\[ID\]|Status: PROVISIONAL FOUNDATION" world systems qa series
rg -n "Arc|Chapter|Scene|Volume" world/WORLD-BIBLE.md systems/SYSTEMS-BIBLE.md
git diff --check
git status --short
git add qa/FOUNDATION-QA.md series/ROADMAP.md
git commit -m "qa: pass red jackal phase 1 foundation"
```

The first search must return no template placeholders in the completed authority documents; the second may return only deliberate scope-boundary wording and must not show actual arc/chapter records.

---

### Task 4: Final verification and handoff

**Files:**
- Verify: `README.md`, `studio/STUDIO-ARCHITECTURE.md`, `series/SERIES-CONSTITUTION.md`, `world/WORLD-BIBLE.md`, `systems/SYSTEMS-BIBLE.md`, `qa/FOUNDATION-QA.md`, `series/ROADMAP.md`

- [ ] **Step 1: Confirm the working tree and commit sequence.**

Run:

```powershell
git status --short
git log --oneline -5
```

Expected: clean working tree and separate commits for the design, world, systems, and QA updates.

- [ ] **Step 2: Re-run the content gate from the repository root.**

Run the exact QA commands recorded in `qa/FOUNDATION-QA.md`. Confirm that all required checks exit successfully and that the roadmap contains no entries.

- [ ] **Step 3: Report the evidence and remaining boundary.**

Summarize the files changed, QA result, commit IDs, and explicitly state that no arcs or chapters were created. Do not claim browser, build, or manuscript validation because this is a Markdown canon foundation.
