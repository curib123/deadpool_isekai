# Reader Copies

Start with `SYNOPSIS.md`, then `volume-001/CH001-WRONG-FOREST-WRONG-WORLD.md`. Greywake covers CH001–CH026. CH027 starts Merrowgate; later chapters have no prose yet. The prologue is optional bonus material and does not precede CH001 in the primary reading sequence.

Copies are generated from `manuscript/`, with front production metadata removed. They are synchronized review copies, not proof of independent gate approval or external posting. The source manifest records both manuscript and reader-copy hashes.

From the repository root:

```sh
python tools/publication.py --sync
python tools/publication.py --check
```

Edit manuscripts first. A semantic change made only in a reader copy fails the check. The checker does not assess literary quality. Dated PASS records under `qa/publish/` belong to prior versions; current scope is recorded in `qa/revisions/2026-10-02-EDITORIAL-REVIEW.md`.
