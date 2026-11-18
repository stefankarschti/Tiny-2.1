"""Run the shared TINY trainer with only the adjacent OSM text facts."""
from pathlib import Path
import json
import re
import runpy
import sys


TRAINING_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TRAINING_DIR))

import gen2


def configure_dataset():
    # gen2 initially loads the base kit's tables. Replace the text facts and
    # disable every table/task generator before the trainer constructs batches.
    gen2.FACTS = str(Path(__file__).resolve().parent / 'facts')
    facts = gen2.load_txt()
    if not facts or any(not f['train_q'] or not f['test_q'] for f in facts):
        raise ValueError('OSM facts must include training and held-back questions')
    for fact in facts:
        for question in fact['train_q'] + fact['test_q']:
            for answer in fact['answers']:
                if (len(question) > 72 or len(question) + len(answer) + 2 > 128
                        or not all(32 <= ord(c) <= 126 for c in question + answer)):
                    raise ValueError('OSM example exceeds TINY limits: ' + question)
    gen2.TXT = facts
    gen2.GENS = [('facts', gen2.g_txt, 1.0)]

    benchmark = json.loads(Path(__file__).with_name('benchmark.json').read_text())
    def normalize(question):
        return tuple(re.findall(r'[a-z0-9]+', question.lower()))
    reserved = {normalize(row['question']) for row in benchmark}
    sample = gen2.sample

    def sample_without_benchmark(rng, test=False, kind=None):
        while True:
            question, answer, category = sample(rng, test, kind)
            if test or normalize(question) not in reserved:
                return question, answer, category

    gen2.sample = sample_without_benchmark


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('train', 'eval', 'export'):
        raise SystemExit('Usage: train.py train MINUTES OUT.pt [--resume MODEL.pt]\n'
                         '       train.py eval MODEL.pt\n'
                         '       train.py export MODEL.pt OUT.BIN')
    configure_dataset()
    runpy.run_path(str(TRAINING_DIR / 'train2.py'), run_name='__main__')
