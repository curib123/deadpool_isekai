# Battle / Scene OA Expansion Design

**Date:** 2026-09-20  
**Project:** This Isekai Has a Bug. Unfortunately, It's Me.  
**Status:** APPROVED IN CHAT — SPECIFICATION FOR REVIEW

## 1. Intent

Strengthen the series' battle and scene planning so every meaningful battle/action chapter has an explicit matchup identity, changing battlefield state, and consequence. Each destination arc must contain a purposeful mixture of minor encounters, major action, and one great/climax battle sequence without forcing combat into chapters whose situations do not create it.

The immediate application is the Merrowgate Arc. Greywake's existing battle map and canon prose remain authoritative and are not rewritten by this change.

## 2. Success Criteria

The revision succeeds when:

1. Every planned Merrowgate battle or meaningful hostile-action chapter has a battle/action card with participants, numerical topology, topology change, terrain, objective, non-combatants/protected targets, turning point, outcome, cost, and scene handoff.
2. Merrowgate contains multiple distinct action structures, including rescue under attack, uneven opposition, split-party action, multi-front crisis, and a natural 2v4/1v4 private-security interception where the numerical disadvantage changes tactics.
3. Merrowgate's great battle is a coordinated two-chapter harbor crisis, not a single Red-versus-Cassian duel. Infrastructure, weather/tide, workers, public authority, private security, evacuation, and evidence all affect the result.
4. At least two non-Red characters own decisive actions in the great battle, and the arc includes encounters where defeating the opposing force is not the primary objective.
5. Future destination arcs have a reusable battle/scene OA template that maps directly to the existing Battle Scene QA Standard and Gate 6–10 workflow.
6. Non-combat chapters remain explicitly marked as non-combat; no fight is added merely to satisfy a topology count.
7. No current manuscript, published copy, chapter order, destination, character identity, power model, or locked mystery state changes as part of this planning revision.

## 3. Locked Constraints

- Red is already overwhelmingly powerful; tension comes from restraint, information, simultaneous objectives, positioning, consequences, and what an instant solution would damage or reroute.
- A serious Red beat is restraint dropping, never a new power stage.
- Supporting characters retain their specialties and independent agency.
- Cassian remains a systems/evidence/political antagonist, not a secret physical equal to Red.
- Battle topology must arise from the situation. The template records variety; it does not mandate every topology in every arc.
- The existing `qa/BATTLE-SCENE-QA-STANDARD.md` remains the governing quality standard.
- Detailed scene architecture remains a Gate 8 deliverable for the active chapter. The new arc map may assign future battle/action structures without pre-empting the production gate.

## 4. Artifacts

### 4.1 Reusable OA template

Create `planning/BATTLE-SCENE-OA-TEMPLATE.md` as the planning contract for future destination arcs. It will contain:

- arc-level Battle Composition Map fields;
- chapter-level battle/action assignment fields;
- matchup-card fields for sides, numerical topology, topology changes, terrain, objectives, protected targets, Red's role, decisive supporting actions, turning point, outcome, cost, and handoff;
- a scene-beat checklist: orientation, first contact, response, complication, choice, turning point, resolution, cost, and handoff;
- topology-variety and Red/supporting-cast checks;
- explicit `NO BATTLE` and `HAZARD ACTION` classifications so non-combat chapters are not mislabelled;
- Gate 6, Gate 7, Gate 8, Gate 9, and Gate 10 handoff rules.

The template will reference existing QA standards rather than duplicate their full prose.

### 4.2 Merrowgate battle/scene OA

Create `qa/VOLUME-002-MERROWGATE-BATTLE-SCENE-AUDIT.md` as the current arc's Battle Composition Map and planning audit. It will distinguish intended future architecture from prose approval and record the following planned encounters:

| Battle ID | Chapter | Intended structure | Scale | Primary purpose |
|---|---|---|---|---|
| V2-B01 | CH-031 | Red + Samir + shipwright crew vs a shifting load/repair hazard; rescue/repair under structural constraints | MINOR ACTION | Establish that Samir owns engineering decisions and that a flashy solution cannot replace load logic |
| V2-B02 | CH-036 | Red + Samir + workers vs a failing dry-dock system with trapped workers, water, and secondary-collapse risk | MAJOR RESCUE ACTION | Make industrial danger and specialist rescue central without turning Red into the sole solution |
| V2-B03 | CH-042 | Red + Iria + Samir + dockworkers vs cascading cargo-transfer failure while access/perimeter control becomes contested | MAJOR REVERSAL | Make the death, injuries, public suspicion, and infrastructure loss irreversible |
| V2-B04 | CH-045 | Red + Samir + trusted workers vs four private-security contractors attempting to interrupt a covert infrastructure inspection | MINOR HOSTILE INTERCEPTION | Use a natural 2v4/uneven fight where protecting the inspection and avoiding exposure matter more than defeating every guard |
| V2-B05 | CH-047 | Harbor Watch, workers, and Red vs simultaneous infrastructure/weather failures plus private-security seizure attempts | MAJOR / GREAT-BATTLE BUILD | Stabilize routes, preserve public response, and prevent emergency authority from becoming a private takeover |
| V2-B06 | CH-048 | Split coalition fronts vs continuing harbor failures, private security, and evidence seizure | CLIMAX | Complete the multi-front harbor crisis; secure evidence and public control while the port keeps functioning |

CH-033 receives a separate `HAZARD ACTION` card (`V2-A01`) for its short warehouse/infrastructure emergency. It is part of action coverage but is not counted as a combat topology or as one of the arc's battle IDs.

The map will identify CH-047→CH-048 as the great battle sequence. Its planned topology changes are:

1. distributed defensive response against environmental/infrastructure failure;
2. split fronts as workers and Harbor Watch protect different routes;
3. private-security interference creates an uneven 2v4/1v4 interception;
4. Red disengages from a winnable physical confrontation to preserve a more important route/evidence objective;
5. the coalition converges on stabilization, evidence security, and public command rather than a boss duel.

The map will also record that CH-030, CH-032, CH-034, CH-035, CH-037–CH-041, CH-043–CH-044, and CH-046 are not battle chapters. Where a chapter contains pressure without a battle, its classification will remain `NO BATTLE` or `HAZARD ACTION` rather than being inflated into combat.

## 5. Roadmap Integration

Update `chapters/VOLUME-002-MERROWGATE-CHAPTER-ROADMAP.md` only at the chapter architecture level:

- add Battle/Scene OA assignments for CH-031, CH-036, CH-042, CH-045, CH-047, and CH-048;
- record the battle IDs and topology for each assigned chapter;
- preserve existing chapter objectives, movement structure, manifestation counts, injury continuity, mystery boundaries, and climax placement;
- mark non-combat chapters explicitly where needed;
- state that detailed scene files are created only when the chapter reaches Gate 8.

No manuscript or publication file is edited by this phase.

## 6. Verification

Before declaring the implementation complete:

- verify every Merrowgate battle ID appears consistently in the arc audit and chapter roadmap;
- verify every planned battle/action card has the required matchup and scene fields;
- verify the arc includes at least one minor action, one major reversal, one great battle sequence, three or more distinct topologies, non-Red decisive actions, and a non-defeat objective;
- verify at least one topology change is present in every major/great encounter;
- verify no `NO BATTLE` chapter receives a combat assignment;
- verify no manuscript, publication, character, mystery, or continuity files changed;
- run `git diff --check` and a focused `rg` consistency scan for battle IDs/topology labels.

## 7. Out of Scope

- rewriting existing Greywake manuscripts or published copies;
- drafting Merrowgate prose;
- creating detailed Gate 8 scene files for inactive chapters;
- adding new powers, stages, enemies, factions, mysteries, or cosmology revelations;
- requiring every arc to use every possible numerical topology;
- replacing the existing Battle Scene QA Standard or broader Gate system.

## 8. Implementation Handoff

After this specification passes review, invoke the writing-plans workflow to produce a file-level implementation plan. The plan must keep the work documentation-first and must not advance any chapter to prose or canonization without its existing production gate.
