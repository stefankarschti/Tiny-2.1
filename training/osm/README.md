# OpenStreetMap mapping training set

The corpus has 1,889 fact records and 7,456 training questions. The 100
workflow records cover mapping practice, editors, geometry and tagging.
Each has three training phrasings, including a new scenario or paraphrase.
The other 1,789 records each define a distinct documented key=value tag.
Each has four template-based training questions. Variants count as questions,
and each tag counts once as a fact. Definitions are sourced via the
[Taginfo API](https://taginfo.openstreetmap.org/taginfo/apidoc).

Each line uses the shared trainer's format:

    training question | other training questions | held-back question => answer

The last phrasing of every record is reserved. All authored prompts fit the
72-character runtime limit and the 128-character question/answer context.
The sampler applies the original typo and phrasing augmentation during training.

## Training

From the repository root, activate the project's Python environment and choose
a new output directory. The following command initializes weights from the
original TINY checkpoint and trains for ten minutes on OSM examples only.

```sh
source .venv/bin/activate
mkdir -p training/osm/models/my-run
python training/osm/train.py train 10 training/osm/models/my-run/osm.pt \
  --resume training/tiny2.pt --lr 5e-4 --decay 0.3
python training/osm/train.py export training/osm/models/my-run/osm.pt training/osm/models/my-run/TINY.BIN
```

Omit the resume and learning-rate options for the shared trainer's from-scratch
defaults. Run the exported model interactively from its model directory:

```sh
make
(cd training/osm/models/my-run && ../../../../build/tiny 0)
```

## Comparing models

`benchmark.json` freezes the 100 original evaluation phrasings and reference
answers. The OSM sampler rejects normalized matches to these questions during
training. The stock trainer evaluates a sample of up to 120 questions drawn
from the larger corpus. To compare native models on the original benchmark,
run the following from the repository root after building the Mac executable:

```sh
.venv/bin/python training/osm/compare.py training/osm/models/run-10m-20261117 \
  training/osm/models/my-run training/osm/models/my-run/comparison.json
```

The output includes every prompt, reference, both answers, exact matches and
keyword scores. Review answers for meaning, negation and syntax. Each test
question refers to a fact whose answer occurs in training.

## Sources

`SOURCES.tsv` lists the initial 20 wiki articles. `TAG_SOURCES.tsv` links each
added tag to its wiki page. English definitions were selected on 2026-11-18
from Taginfo's key/values API (top 250 values by usage per queried key),
requiring wiki documentation, English text, printable ASCII and a definition
that fits the model context. The tag prompts are generated from the key/value
strings. The descriptions are short wiki-derived text, not independently
verified field observations. Source pages can change.

See [license and attribution](LICENSE.md) and [validation counts](VALIDATION.json).
