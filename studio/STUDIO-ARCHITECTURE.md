# Red Jackal Light-Novel Studio Architecture

## Governance
This repository uses a studio-style production pipeline. Each agent has an editorial-equivalent role, owned canon domain, inputs, outputs, and a QA gate.

## Canon hierarchy
Series Constitution → World Bible → Systems/Lore → Character Bible → Mystery Bible → Destination → Volume/Arc → Chapter → Scene → Manuscript → QA → Canon → Publication Copy → Publish Version QA → Release.

Lower levels cannot silently contradict higher levels.

## Agent Registry

| ID | Agent | Studio-equivalent role | Ownership |
|---|---|---|---|
| A001 | Series Director | Executive Story Editor / Showrunner | series identity, major canon |
| A002 | Lead Editor | Managing Editor | workflow and approval gates |
| A010 | World Bible Director | Lead Worldbuilding Editor | macro world bible |
| A011 | Geography Editor | Setting Geography Designer | continents, seas, map logic |
| A012 | Nations & Politics Editor | Political Worldbuilding Editor | states and diplomacy |
| A013 | Culture Editor | Cultural Setting Designer | culture and customs |
| A014 | Economy & Travel Editor | Logistics Editor | currency, routes, travel time |
| A015 | Monster Ecology Editor | Bestiary Designer | monsters and ecology |
| A020 | World History Director | Lore Historian | chronology and historical truth |
| A021 | Reincarnation Historian | Cosmology Lore Editor | soul/reincarnation history |
| A030 | Cosmology Director | Mythology Editor | metaphysical hierarchy |
| A031 | World System Architect | System Mechanics Designer | normal System rules |
| A032 | Magic System Architect | Magic Mechanics Designer | magic rules |
| A033 | Fate Architect | Metaphysical Systems Designer | Fate |
| A034 | Great Design Architect | Endgame Mythology Designer | Great Design |
| A035 | Anomaly Architect | Exception Designer | Red Jackal anomaly |
| A036 | Imagination Power Designer | Signature Ability Designer | Play Logic |
| A037 | Power Balance Editor | Combat Systems QA | limits/counters/escalation |
| A040 | Character Bible Director | Lead Character Editor | character canon |
| A041 | Character History Editor | Backstory Editor | histories and motives |
| A042 | Character Arc Editor | Development Editor | growth/relationships |
| A043 | Red Jackal Guardian | Lead Protagonist Editor | Red Jackal consistency |
| A044 | Supporting Cast Editor | Ensemble Editor | supporting cast autonomy |
| A045 | Antagonist Editor | Villain Development Editor | antagonist quality |
| A050 | Mystery Director | Series Mystery Editor | mystery architecture |
| A051 | Foreshadowing Editor | Setup/Payoff Editor | clue planting/payoffs |
| A060 | Destination Director | Location Scenario Planner | destination eligibility |
| A061 | Arc Architect | Arc Scenario Writer | destination-arc structure |
| A062 | Destination Culture QA | Location Continuity Editor | uniqueness |
| A063 | Local Story Editor | Arc Story Editor | local conflict/resolution |
| A064 | Travel Editor | Journey Scenario Editor | between-arc travel |
| A070 | Series Roadmap Director | Long-Range Planner | provisional roadmap |
| A071 | Volume Editor | Volume Scenario Editor | volume architecture |
| A072 | Pacing Editor | Narrative Pacing Editor | action/downtime balance |
| A080 | Chapter Architect | Chapter Planner | chapter sheets |
| A081 | Scene Architect | Scene Planner | scene purpose/change |
| A090 | Manuscript Author | Light-Novel Writer | prose draft |
| A091 | Red Jackal Voice Writer | Character Voice Specialist | first-person voice |
| A092 | Dialogue Editor | Dialogue Specialist | dialogue |
| A093 | Comedy Editor | Comedy/Timing Editor | natural humor |
| A094 | Reference Editor | Cultural/Reference Editor | pop-culture references |
| A095 | Action Choreographer | Battle Scene Editor | combat clarity |
| A096 | Imagination Scene Designer | Signature Action Designer | Play Logic scenes |
| A097 | Prose Editor | Line Editor | natural prose |
| A098 | Publication Editor | Release Copy Editor | canon-derived platform-ready publication copies |
| A100 | Continuity Director | Continuity Editor | continuity ledger |
| A101 | Canon Conflict Detector | Canon QA Editor | contradictions |
| A102 | Knowledge-State Editor | Information-State Editor | who knows what |
| A110 | Legal/Reference QA | Rights/Reference Editor | copying/reference risks |
| A111 | Logic Editor | Plausibility Reviewer | world/social logic |
| A120 | Chapter QA Editor | Manuscript QA Editor | chapter gate |
| A121 | Volume QA Editor | Volume Review Editor | volume gate |
| A122 | Arc QA Editor | Arc Review Board | destination-arc gate |
| A123 | Series QA Board | Senior Editorial Board | full-series audit |
| A124 | Publish Version QA Editor | Release QA Editor | canon-equivalent reader-facing publication checks |
| A130 | Canon Librarian | Story Bible Manager | authoritative records |

## Production Flow
### Phase 1 Foundation
Series Director → World Bible Director → Geography → History → Cosmology → System → Magic → Fate → Great Design → Nations → Cultures → Economy/Travel → Bestiary → Foundation QA.

### Phase 2 Characters
Character Bible Director → Red Jackal Guardian → Supporting Cast → Antagonists → Character Histories → Relationships → Character QA.

### Phase 3 Mystery
Mystery Director → Writer Truth → Mystery IDs → Foreshadowing IDs → Reveal plan → Payoff plan → Mystery QA.

### Phase 4 Destination Inventory
Destination Director catalogs existing World Bible places → Geography/Politics/Culture/Travel review → Mystery-dependency review → Classification (HIGH POTENTIAL / RESERVED / UNUSED / NOT SUITABLE) → Destination Inventory QA.

### Destination Selection Gate
After Phase 4 passes: compare eligible DEST records → choose one existing destination → clear RESERVED dependencies if applicable → validate local-story capacity and travel logic → Destination Selection QA.

No destination becomes an arc before this selection gate passes.

### Phase 5 Volume/Arc
Arc Architect → Volume Editor → Pacing Editor → Character Arc Editor → Mystery Editor → Power Balance Editor → Volume/Arc QA.

### Phase 6 Chapter
Chapter Architect → Scene Architect → Continuity precheck → Knowledge-state check → Foreshadowing check → plan approval.

### Phase 7 Manuscript
Manuscript Author → Red Jackal Voice → Dialogue → Comedy → Action → Reference → Prose.

### Phase 8 QA
Canon Conflict → Continuity → Power → Mystery → Character → Paragraph → Reference → Chapter QA.

### Phase 9 Canonization
Lead Editor approval → Series Director approval if high-level canon changed → Canon Librarian updates authoritative records.

### Phase 10 Publication Copy
Publication Editor derives a reader-facing copy from the latest CANON manuscript → removes repository metadata → applies target-platform-safe formatting only → records canon source revision.

Publication edits must remain semantically equivalent to canon.

### Phase 11 Publish Version QA
A124 Publish Version QA Editor → canon-equivalence diff → title/order/ending check → metadata-removal check → paragraph/dialogue/emphasis check → platform-readability check → copyright/reference check → **PUBLISH-READY — GATE 11 PASS**.

If a requested release edit changes story meaning, it must return to Manuscript QA and canonization before a new publication copy is generated.

## No-Skip Rule
Major ideas may not jump directly from idea to prose. Route them through the department that owns the affected canon.

## QA Escalation
Prose issue → A097. Dialogue → A092. Character → A040/A043. Power → A031-A037. World → A010. Arc → A061. Publication formatting/canon-equivalence → A124. Major series contradiction → A001.

## Canon States
LOCKED, CANON, PROVISIONAL, PLANNED, DRAFT, PUBLISH DRAFT, PUBLISH-READY, PUBLISHED, DEPRECATED.

## Single Source of Truth
Each canon domain has one authoritative Bible. Other documents reference it; they do not redefine it.
