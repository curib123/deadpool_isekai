# Editorial Revision — 2026-10-02

**Base:** e084a1c00eebc10c8fb8aeb13a36313fdc26f801.
**Scope:** Current prose CH001–CH027, optional prologue, reader copies, active story maps, continuity and power/mystery authority.
**State:** Revision prepared for author review. This record does not claim independent studio gate approval, external posting or proven reader reception.

## Problems addressed

The September reset named Rook Vane and Fortune Distortion in manuscript headers while several bodies still used conjured barriers/tools, automatic restoration and overwhelming strength. All 26 public Greywake chapters and the synopsis still described the previous Red Jackal version. The prologue used first-person narration and a time pause. Active plans, clue meanings and old PASS wording contradicted the new mechanics.

## Story changes

- Fully reworked CH001, CH002, CH010, CH015, CH022–CH024 and the optional prologue. The opening begins with immediate predator pressure; the intake is shorter; the audit starts with Rook's omitted injury; the climax has overlapping rescue, road and evidence objectives.
- Targeted repairs in CH003, CH005, CH006, CH009, CH016–CH018, CH020–CH021, CH025–CH027 remove incompatible abilities, clarify causal choices, connect reputation to new obligations, or improve handoffs.
- CH004, CH007, CH008, CH011–CH014 and CH019 retain their substantive story, with current front metadata and whitespace normalization. This is not a full line edit of every paragraph.
- Rook chooses his alias in CH001 and repeats it at the gate. He arrives without local coins or a knife. The old Earth name is retired rather than promised as a future reveal.
- CH015 keeps a deliberate violation of Brynn's order. Rook uses a technician's pry bar, and a failing band lets him extract the lure. Luck helps the action happen; the responsibility stays his.
- CH016 preserves backflow, destroyed bridge and Kellan's severe injury. Rook uses a harness and real cart sideboard; the rescue uses a lever and multiple people. CH017/CH025 treatment and CH026/CH027 recovery are ordinary.
- CH022–CH024 replace manifestations and monster wrestling with panels, ropes, hooks, timber, jacks, witnesses and specialists. Each lucky jam has a visible object and limited duration. No commandable outcome, guaranteed objective or second ability is introduced.
- Merrowgate retains CH027–CH050 and its planned evidence window, but its mechanical plan is rewritten for luck only. Rook's paid delivery and receipt connect him to the sabotage; rescue cannot erase liability. Only CH027 has prose.

## Continuity decisions checked

| Thread | Revised evidence |
|---|---|
| System identity | CH002 retains two independent controls and the full UNDEFINED / UNAVAILABLE / NO RECORD / FAILED / ANOMALY readout. CH003 keeps normal physical measurement separate from identity. No later chapter grants a valid root. |
| Translation | Speech is mediated by charged Wayfarer Tongue Tokens. Writing remains unreadable; the ferry fee and intake hook respect this restriction. |
| Injury | Forest cut/ankle, CH007 stitches, CH015 new cut, CH016 shoulder impact, climax hand/knee injuries and normal travel recovery remain distinct from Kellan's fractures. |
| Decision and aftermath | Warning in CH014/CH015 → intentional extraction → shifted calls → backflow → bridge loss → medical and political consequences. |
| Agency | Tavian reads movement; Brynn commands/restrains; Kellan engineers from a cot; Jessa chooses testimony/settings; Maelis preserves records; workers make lasting repairs. |
| Objects | Pry bar borrowed from the case; packing block from storehouse; beams/panels/rope staged by crews; jack and real braces carry shelf load. No vanished support or created equipment. |
| Knowledge | Cast retains observations and hypotheses, not writer knowledge of Soul Drift, Fate, Savael or Great Design. Maelis's correlation ledger is evidence collection, not definitive statistical proof. |
| Foreshadowing | F-001 CH002 and F-002 CH003 remain. F-004 CH005 and F-003 CH007 receive explicit luck-only definitions. M-004/M-005/M-006 and F-012/F-018 are retired. F-010 remains planned for unwritten CH038. |
| Destination | Greywake ends at CH026. CH027 carries money, wounds, supplies and documentation into Merrowgate; its guarantor hook does not introduce new cast encounters or a planted clue. |

## Verification

Executed successfully:

```sh
python tools/publication.py --sync
python tools/publication.py --check
python -m py_compile tools/publication.py
git diff --check
```

The synchronized set contains 28 reader copies: 27 ordered chapters plus the optional prologue, totaling 50,406 body words under the utility's word-count convention. Source and copy SHA-256 values are recorded in `published/SOURCE-MANIFEST.json`. Copies contain title and story body; production metadata remains in the source.

A temporary copy-only edit was rejected with a reader/source mismatch; the original file was restored and the clean check rerun. The utility also checks for known retired-power prose markers and unexpected reader chapters. It is a targeted guard, not a general proof of literary or semantic correctness.

Reviewed the rewritten units and targeted repairs against the current causal chain and knowledge boundaries. Current Markdown links were checked for missing local targets. No external website or serial platform was updated.

## Remaining review scope

Earlier detailed scene plans and manhwa assets are historical and explicitly require adaptation before production. Prior dated PASS reports remain historical; they are not inherited by revised text. The rewritten scene notes summarize the new units without pretending to have received separate departmental reviews.

An independent full-volume line edit, author taste review and complete future-chapter scene design remain separate work. No CH028–CH050 prose is claimed. The revision preserves the existing story's outcomes while changing how Rook earns opportunities and what those opportunities cost.
