#!/usr/bin/env python3
"""Synchronize and verify reader copies against the manuscript. Standard library only."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'published' / 'SOURCE-MANIFEST.json'
FRONT_FIELDS = re.compile(r'^\*\*(?:Status|Revision Date|Word Count|Chapter QA|Retcon QA|Battle QA|Volume|POV|Review):\*\*', re.M)
REMOVED_PROSE = [
    r'\bRed Jackal\b', r'\bEvan Calder\b', r'\bPlay Logic\b',
    r'\bFourth-Wall Pause\b', r'\bJackal Luck\b',
    r'pale-grey (?:material|guide|support|deflector|block|obstruction|rail)',
    r'dark material folded', r'could (?:have )?(?:erase every predator|ripped the recess|thrown the whole wreckage)',
    r'(?:wounds?|injuries) (?:were |had )?(?:already )?(?:disappear|almost gone)',
    r'editing damage out of existence', r'already restoring yourself',
    r'the impossible answer was still there', r'the horse finished its step',
]


def reader_text(source):
    lines = source.read_text(encoding='utf-8').splitlines()
    if not lines or not lines[0].startswith('# '):
        raise ValueError(f'Missing title: {source.name}')
    index = 1
    while index < len(lines) and (not lines[index].strip() or FRONT_FIELDS.match(lines[index])):
        index += 1
    body = '\n'.join(lines[index:]).strip()
    if not body:
        raise ValueError(f'Empty chapter: {source.name}')
    return lines[0] + '\n\n' + body + '\n'


def mappings():
    chapters = sorted((ROOT / 'manuscript').glob('CH[0-9][0-9][0-9]-*.md'))
    ids = [int(p.name[2:5]) for p in chapters]
    if ids != list(range(1, 28)):
        raise ValueError(f'Expected one source per CH001–CH027; got {ids}')
    result = []
    for source in chapters:
        volume = 'volume-001' if int(source.name[2:5]) <= 26 else 'volume-002'
        result.append((source, ROOT / 'published' / volume / source.name))
    result.append((ROOT / 'manuscript/SERIES-PROLOGUE-THE-WRONG-PERSON.md',
                   ROOT / 'published/PROLOGUE-THE-WRONG-PERSON.md'))
    return result


def record(source, target, prose):
    return {
        'source': str(source.relative_to(ROOT)),
        'reader_copy': str(target.relative_to(ROOT)),
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'reader_sha256': hashlib.sha256(prose.encode('utf-8')).hexdigest(),
        'body_words': len(re.findall(r"\b[\w]+(?:['’][\w]+)?\b", prose.split('\n\n', 1)[1])),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--sync', action='store_true', help='Write reader copies and source manifest')
    mode.add_argument('--check', action='store_true', help='Verify without changing files')
    args = parser.parse_args()
    errors, records = [], []
    try:
        pairs = mappings()
    except ValueError as exc:
        parser.exit(1, str(exc) + '\n')
    expected_targets = {target for _, target in pairs}
    actual_targets = set((ROOT / 'published').glob('volume-*/CH[0-9][0-9][0-9]-*.md'))
    for extra in sorted(actual_targets - expected_targets):
        errors.append(f'Unexpected reader chapter: {extra.relative_to(ROOT)}')
    for source, target in pairs:
        prose = reader_text(source)
        records.append(record(source, target, prose))
        for pattern in REMOVED_PROSE:
            if re.search(pattern, prose, re.I):
                errors.append(f'Retired prose marker in {source.name}: {pattern}')
        if FRONT_FIELDS.search(prose.split('\n\n', 1)[1]):
            errors.append(f'Production metadata leaked: {source.name}')
        if args.sync:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(prose, encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8') != prose:
            errors.append(f'Reader/source mismatch: {target.relative_to(ROOT)}')
    payload = {'revision': '2026-10-02', 'scope': 'CH001–CH027 and optional prologue', 'files': records}
    if args.sync and not errors:
        MANIFEST.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    elif args.check:
        try:
            if json.loads(MANIFEST.read_text(encoding='utf-8')) != payload:
                errors.append('Source manifest is stale; run --sync')
        except (FileNotFoundError, json.JSONDecodeError):
            errors.append('Missing or invalid source manifest; run --sync')
    if errors:
        parser.exit(1, '\n'.join(errors) + '\n')
    words = sum(item['body_words'] for item in records)
    print(f'{"Synced" if args.sync else "Verified"}: {len(pairs)} reader copies, '
          f'27 ordered chapters + optional prologue, {words:,} body words. '
          'Editorial quality and independent gate approval are separate.')


if __name__ == '__main__':
    main()
