# Flexible Arc Endgame Readiness

**Owners:** A070 Series Roadmap Director, A122 Arc QA Board, A123 Series QA Board  
**Supporting owners:** A001 Series Director, A050 Mystery Director, A060 Destination Director, A061 Arc Architect, A100 Continuity Director, A102 Knowledge-State Editor, A124 Publish Version QA Editor  
**Status:** ACTIVE — CURRENT VERDICT NOT READY  
**Authority:** `docs/superpowers/specs/2026-09-20-flexible-series-arc-architecture-design.md`

## 1. Current Verdict

| Control | Current state |
|---|---|
| Flexible future route | **ACTIVE / PROVISIONAL** |
| Arc 1 — Greywake | **COMPLETE / RELEASE-READY** |
| Arc 2 — Merrowgate | **LOCKED / IN PRODUCTION** |
| Future destinations | **NOT SELECTED** |
| Final arc | **NOT READY** |
| Series stop condition | **NOT YET SATISFIED** |
| Immediate production authorization | **CH-027 synchronization → Gate 9** |

Machine-readable authority state:

```text
Future destinations: NOT SELECTED
Final arc: NOT READY
Series stop condition: NOT YET SATISFIED
Immediate production authorization: CH-027 synchronization → Gate 9
```

## 2. Arc-Admission Checklist

A provisional story-function slot may become a destination arc only when every row passes:

| Requirement | Result | Required evidence |
|---|---|---|
| Existing eligible World Bible place | NOT YET for future slots | Destination Inventory record |
| Destination Selection Gate 5 | NOT YET for future slots | Gate 5 QA record |
| Distinct culture and visual identity | NOT YET for future slots | Destination/World/Culture review |
| Local conflict that matters without Red | NOT YET for future slots | Gate 6 volume architecture |
| Travel entry and exit logic | NOT YET for future slots | Travel Editor review |
| Mystery-safe window | PROVISIONAL | Future Mystery-Window Schedule + Gate 6/7 approval |
| Supporting-cast autonomy | PROVISIONAL | Character distribution and knowledge matrix |
| Battle Composition Map where combat naturally occurs | PROVISIONAL | Battle Topology Ledger + Gate 6 |
| Volume/Arc Gate 6 | NOT YET for future slots | Gate 6 QA record |
| Chapter Roadmap Gate 7 | NOT YET for future slots | Gate 7 QA record |
| No higher-level contradiction | REQUIRED | Foundation, continuity, systems, mystery, and series QA |

## 3. Merge and Cut Checklist

Document a merge or cut decision when any of the following becomes true:

- two candidate destinations perform the same local and mystery function;
- a slot exists only to host a reveal, stronger opponent, or scenic battle;
- the midpoint and climax repeat a previous pressure pattern;
- the local resolution is complete before the planned ending;
- the slot can be removed without damaging the mystery ladder, native story, or consequence chain.

**Current merge/cut decisions:** None. All future slots remain provisional and unselected while destination evidence is gathered.

## 4. Final-Arc Readiness Checklist

| Requirement | Result | Evidence required before PASS |
|---|---|---|
| M-001 through M-012 receive authorized payoffs | NOT READY | Mystery Director payoff map and canon evidence |
| Protected F-IDs have planting and payoff records | NOT READY | Chapter/scene records plus Gate 9/10 |
| Native Hero/Party story has independent resolution | NOT READY | Native-story consequence and resolution record |
| Red remains an outsider/Story Intruder, not a conventional chosen Hero | NOT READY | Character, native-story, and final manuscript QA |
| Final structural choice has demonstrated consequences | NOT READY | Endgame architecture and continuity ledger |
| Final destination passes Gate 5 | NOT READY | Destination Selection QA |
| Final volume passes Gate 6 and Gate 7 | NOT READY | Volume and chapter QA |
| Final scenes pass Gate 8 and Gate 9 | NOT READY | Scene and manuscript QA |
| Canon and knowledge state pass Gate 10 | NOT READY | Series QA |
| Reader-facing release passes Gate 11 | NOT READY | Publish Version QA |
| No extra explanatory arc is required | NOT READY | Series QA Board stop decision |

## 5. Series Stop Condition

The series may stop only when:

1. Authorized payoffs for M-001 through M-012 are complete without contradiction.
2. The protected F-ID planting/payoff chain is evidenced.
3. The native Hero/Party story reaches a legitimate resolution independent of Red's identity.
4. The final structural choice affects Red and Veyr and is not consequence-free.
5. The final destination resolves its own local conflict and aftermath.
6. The final arc preserves the rule that Red is not converted into a conventional chosen Hero.
7. No additional arc is needed to explain, soften, or repeat the ending.

## 6. Gate Sequence

Future work must proceed through:

**Destination Selection Gate 5 → Volume/Arc Gate 6 → Chapter Roadmap Gate 7 → Scene Gate 8 → Manuscript Gate 9 → Canon Gate 10 → Publish Version Gate 11**

No later gate can authorize a missing earlier gate. This readiness record cannot authorize a destination, chapter, manuscript, or publication copy by itself.

## 7. Linked Controls

- `planning/FLEXIBLE-FUTURE-ARC-REGISTRY.md`
- `planning/FUTURE-MYSTERY-WINDOW-SCHEDULE.md`
- `continuity/SERIES-CONSEQUENCE-LEDGER.md`
- `planning/BATTLE-TOPOLOGY-LEDGER.md`
- `series/ROADMAP.md`
- `planning/STORY-PLANNING.md`
- `qa/QA-GATES.md`
- `qa/PUBLISH-VERSION-QA-STANDARD.md`
