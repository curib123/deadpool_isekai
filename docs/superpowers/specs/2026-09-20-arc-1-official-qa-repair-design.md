# Arc 1 Official QA and Repair Design

**Date:** 2026-09-20  
**Scope:** Volume 1 / Greywake Arc / CH-001 through CH-026  
**Status:** Design approved in chat; implementation pending spec review  
**Source:** User-provided revised Official Arc 1 QA Checklist

## 1. Purpose

Apply the revised 40-section Arc 1 checklist to the existing Greywake manuscripts, scene architectures, continuity records, battle records, and publication QA. Repair confirmed weaknesses or missing requirements using the smallest effective change while preserving locked canon.

This is an editorial QA and targeted-repair pass. It is not permission to add filler chapters, force battle topologies, invent powers, rewrite Red into a conventional hero, or expand Arc 1 with unrelated lore.

## 2. Scope Boundary

### Included

- `manuscript/CH001...CH026`
- `scenes/CH-001...CH-026`
- Greywake roadmap, architecture, continuity, mystery, battle, Gate 9, Gate 10, and Gate 11 records
- `published/volume-001` only for canon-equivalence verification and QA-record synchronization
- A new authoritative Arc 1 checklist record: `qa/VOLUME-001-GREYWAKE-OFFICIAL-ARC-1-QA.md`

### Excluded

- CH-027 and the Merrowgate manuscript synchronization problem
- Volume 2 prose or future chapter drafting
- New chapters, new named characters, new powers, or new factions unless an existing locked record proves one is required
- Publication prose changes when the current publication body is already canon-equivalent

## 3. Authority and Conflict Rules

The studio hierarchy remains authoritative: Series Constitution → World/System/Character/Mystery Bibles → Greywake architecture/roadmap → scene architecture → manuscript → QA → publication copy.

The checklist cannot override locked canon. In particular:

- Red remains already overpowered; tension comes from objectives, information, restraint, consequences, and other actors.
- Red has no conventional moral-development or power-progression arc. “MC changes slightly” is satisfied only through knowledge, tactics, relationships, choices, or consequences that preserve his core identity.
- Battle variety is situational, not a quota. Existing 1v1, team, rescue, defense, multi-front, and tactical structures remain valid; no artificial 1v4 is required.
- Death, injury, civilian harm, infrastructure damage, mystery boundaries, and knowledge limits remain consequential.
- A conflict between a current manuscript and a stale QA record is repaired at the earliest authoritative source, then downstream QA is re-run.

## 4. QA Record Contract

Create one checklist record containing all 40 sections from the user-provided checklist, including the ten-point production gate.

Each section uses exactly one primary status:

- `PASS` — the current Arc 1 record and manuscript evidence satisfy the item.
- `WEAK` — the element exists but needs a targeted improvement.
- `MISSING` — the element is important and absent.
- `N/A` — the checklist item is intentionally not required for Greywake; include a reason.

Every `WEAK` or `MISSING` item must have a directly adjacent `FIX:` line using:

`Problem → Cause → Best Chapter → Smallest Effective Fix → Continuity Check → Re-QA`

Optional battle-variety choices may be `N/A` when Greywake does not naturally support them. Mandatory sections may not be silently skipped.

## 5. Repair Strategy

1. Audit the existing manuscripts and current QA records against the checklist.
2. Separate actual story weaknesses from stale documentation or historical QA language.
3. Prefer a multi-purpose repair inside an existing scene or aftermath beat.
4. Repair the earliest source of any continuity or authority contradiction.
5. Re-run affected chapter Gate 9, battle/scene QA, volume Gate 10, and publication Gate 11 checks.
6. Update the Arc 1 checklist record with final evidence and remaining intentional `N/A` items.

Documentation-only repairs must not be described as manuscript improvements. Manuscript repairs must identify the exact affected chapter and preserve its locked event, scene order, character knowledge, mystery state, and ending unless the owning authority explicitly changes.

## 6. Known Starting Conditions

The fresh recheck found:

- CH-001 through CH-026 are current first-person manuscripts with individual Gate 9 records.
- The 26 Volume 1 publication bodies are currently body-equivalent to the manuscripts.
- Aggregate Volume 1 Gate 10/Gate 11 records contain stale/historical status language that needs synchronization.
- CH-017 through CH-026 publication QA records need current source/copy revision metadata refresh even though their reader-facing bodies match.
- CH-027 is explicitly excluded from this Arc 1 pass and remains a separate synchronization task.

These findings are starting conditions, not assumed final checklist results. The checklist audit must still evaluate the narrative requirements directly.

## 7. Acceptance Criteria

- All 40 checklist sections appear in the authoritative Arc 1 QA record.
- Every `WEAK` or `MISSING` item has a directly adjacent `FIX:` line.
- Every mandatory item is either `PASS` after evidence-based repair or remains visibly `WEAK`/`MISSING` with an actionable fix and reason for deferral.
- The ten-point gate has an evidence-backed result; it is not inflated by treating unresolved mandatory weaknesses as PASS.
- No artificial chapter, battle, power, character, mystery, or tragedy is added merely to make a box green.
- CH-001 through CH-026 continuity, Gate 9, battle QA, Gate 10, and Gate 11 records are internally synchronized after repair.
- The final verification command reports the exact checklist result, affected files, and clean working tree.
