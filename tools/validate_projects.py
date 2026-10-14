#!/usr/bin/env python3
"""Check documents/BOM and optionally compile extracted Arduino sketches."""
import argparse
import ast
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--arduino-cli', help='Installed Arduino CLI executable')
    parser.add_argument('--arduino-config', help='CLI YAML with installed AVR core/libraries')
    args = parser.parse_args()
    bom = json.loads((ROOT / 'procurement-bom.json').read_text())
    total = 0
    ids = set()
    for row in bom['items']:
        assert row['id'] not in ids, row['id']
        ids.add(row['id'])
        assert row['quantity'] > 0 and row['unit_lkr'] >= 0
        assert row['subtotal_lkr'] == row['quantity'] * row['unit_lkr'], row['id']
        assert row['price_basis'] in {'S', 'P', 'E'}
        total += row['subtotal_lkr']
    assert total + bom['delivery_allowance_lkr'] + bom['contingency_lkr'] == bom['budget_lkr']
    plan = (ROOT / 'README.md').read_text()
    assert plan == (ROOT / 'School_Electronics_Club_Procurement_Plan_LKR_50000.md').read_text()
    for row in bom['items']:
        assert f"| {row['id']} |" in plan
    assert f'**LKR {total:,.0f}' in plan
    for category in 'ABCDEF':
        subtotal = sum(row['subtotal_lkr'] for row in bom['items'] if row['category'] == category)
        assert f'— LKR {subtotal:,.0f}' in plan
    print(f"BOM: {len(ids)} rows, items LKR {total:,}; allocation balances to LKR {bom['budget_lkr']:,}.")
    print('Both procurement documents match.')
    projects = sorted((ROOT / 'projects').glob('project-*.md'))
    assert [int(path.name.split('-')[1]) for path in projects] == list(range(1, 21))
    sketches = []
    python_count = 0
    for path in projects:
        text = path.read_text()
        assert '## Complete wiring and power' in text, path
        assert '## Build, test and acceptance checks' in text, path
        assert '## Verification status' in text, path
        for code in re.findall(r'```python\n(.*?)```', text, re.S):
            ast.parse(code, filename=str(path))
            python_count += 1
        for code in re.findall(r'```cpp\n(.*?)```', text, re.S):
            sketches.append((path, code))
    assert python_count == 5 and len(sketches) == 14
    # Links in the historical audit describe the older documents, but still resolve.
    for path in list(ROOT.glob('*.md')) + projects:
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' in link or link.startswith('#'):
                continue
            target = link.split('#')[0]
            assert (path.parent / target).exists(), (path, target)
    print('All 20 guides present; local Markdown links resolve; 5 Python blocks parse.')
    print('Python parsing does not compile MakeCode APIs or test hardware.')
    if not args.arduino_cli:
        print('AVR compilation skipped; pass --arduino-cli and optionally --arduino-config.')
        return
    cli = [args.arduino_cli]
    if args.arduino_config:
        cli += ['--config-file', args.arduino_config]
    with tempfile.TemporaryDirectory(prefix='electronics-sketches-') as temporary:
        work = Path(temporary)
        for path, code in sketches:
            name = 'project_' + path.name.split('-')[1]
            sketch = work / name
            sketch.mkdir()
            (sketch / (name + '.ino')).write_text(code)
            for board in ('arduino:avr:uno', 'arduino:avr:nano:cpu=atmega328'):
                result = subprocess.run(cli + ['compile', '--fqbn', board, str(sketch)],
                                        text=True, capture_output=True)
                if result.returncode:
                    print(result.stdout)
                    print(result.stderr)
                    raise SystemExit(f'Compilation failed: {path.name} / {board}')
                print(f'PASS {name} / {board}', flush=True)
    print('All 14 Arduino sketches compile for both Uno and classic Nano (28 builds).')


if __name__ == '__main__':
    main()
