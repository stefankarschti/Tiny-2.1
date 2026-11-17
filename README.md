# TINY 2.1 — a transformer for DOS

![TINY 2.1 running under DOS](tiny21.png)

A tiny question-answering transformer written in Turbo C 2.0. It runs on a
Pentium or 486DX under plain DOS and fits on a floppy disk.

- 367,000 parameters: 4 layers, 96 wide, reads and writes letter by letter
- 8-bit weights (one scale per row), 380 KB in all
- Needs about 540 KB of free conventional memory
- Trained on about 3,500 facts, each asked in many wordings
  Outside those it makes things up confidently
- Neon full-screen interface with a live neural monitor and a PC-speaker
  robot voice

Written by Fable 5.2 and trained by Opus 5.5.

## Run on Mac

Run the model natively in Terminal on Apple Silicon or Intel Macs. No DOS
emulator, Python, or PyTorch is needed. Install Apple's Command Line Tools
with `xcode-select --install` if you do not already have a C compiler and Make.

```sh
./run-mac.sh
./run-mac.sh 0       # deterministic answers; default creativity is 5
```

The launcher builds `build/tiny` when needed and loads the included
`dos/TINY.BIN`. You can invoke the launcher from any directory. Type `QUIT`
or press Ctrl-D to exit. File input also works:

```sh
./run-mac.sh 0 < questions.txt > answers.txt
```

The Mac version uses the existing plain-text interface, including prompts
and timing information. The neon full-screen interface, function-key controls,
and PC-speaker sounds remain DOS-only. Questions are independent; it does not
remember previous answers. To build without launching, run `make`; `make clean`
removes the generated executable.

## Run on DOS

Copy the files from the `dos` folder to the DOS machine, then:

```
C:\> CD \TINY
C:\TINY> TINY
```

Keep `TINY.EXE` and `TINY.BIN` in the same folder. `dos/README.TXT` has the
keys, options and details. To rebuild: `TCC -ml TINY.C`

## Train it yourself

The `training` folder is the complete training kit: the facts, the
generator that turns them into question/answer pairs in many wordings
(`gen2.py`), and the PyTorch training script (`train2.py`). Needs Python 3,
NumPy and PyTorch; a normal CPU is enough.

```
cd training
python3 gen2.py                                   # show sample questions
python3 train2.py train 60 more.pt --resume tiny2.pt --lr 5e-4 --decay 0.3 --eval-every 20
python3 train2.py eval more.pt
python3 train2.py export more.pt TINY.BIN         # TINY.EXE reads the new file
```

Add your own facts to `training/facts/` (format in `training/TRAINING.TXT`).
Exporting `tiny2.pt` unchanged gives exactly the released `TINY.BIN`.

## Licence

Code: MIT (`LICENSE`). Three data files derived from public datasets keep
their own licences (ODbL and CC BY-SA); see `DATA_LICENSES.md`.
