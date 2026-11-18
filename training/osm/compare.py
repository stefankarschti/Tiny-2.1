"""Compare exported TINY.BIN models on the frozen original OSM questions."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent))
from train2 import correct


def evaluate(model_directory, benchmark):
    prompts = [row['question'] for row in benchmark]
    result = subprocess.run([str(ROOT / 'build/tiny'), '0'], cwd=model_directory,
                            input='\n'.join(prompts + ['quit']) + '\n',
                            capture_output=True, text=True, check=True)
    answers = re.findall(r'\n>   ([^\n]*)\n   \[\d+ letters', result.stdout)
    if len(answers) != len(prompts):
        raise ValueError(f'Expected {len(prompts)} answers, got {len(answers)}')
    return answers


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before', type=Path, help='directory containing the baseline TINY.BIN')
    parser.add_argument('after', type=Path, help='directory containing the new TINY.BIN')
    parser.add_argument('output', type=Path, help='where to save the paired JSON results')
    args = parser.parse_args()
    benchmark = json.loads((HERE / 'benchmark.json').read_text())
    for name in ('before', 'after'):
        answers = evaluate(getattr(args, name), benchmark)
        for row, answer in zip(benchmark, answers):
            row[name] = answer
            row[name + '_exact'] = answer == row['reference']
            row[name + '_keyword'] = correct(row['question'], answer, [row['reference']], 'facts')
        print(name, {m: sum(r[name + '_' + m] for r in benchmark) for m in ('exact', 'keyword')})
    args.output.write_text(json.dumps(benchmark, indent=2) + '\n')
