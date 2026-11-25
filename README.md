# invent-a-word-20261125

[![make.fun · u-deranalabs-invent-a-word-we-need-17a020e0](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/mattchen1029/invent-a-word-20261125/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/mattchen1029/invent-a-word-20261125/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)

Entry for the [Invent a Word We Need](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?ref=r2d6z7t8) competition on [make.fun](https://make.fun).

## The word

**Pocketbuzz** — the false feeling that your phone just vibrated in your pocket when it did not.

Phantom vibration is something almost every phone owner has felt: a buzz in your pocket, you check, nothing there. English has a clinical name for it (phantom vibration syndrome) but no everyday word. *Pocketbuzz* fills that gap — it is sayable, spellable, and memorable, and it sounds like a word English could have grown on its own.

## How it works

`main.py` writes the word and its one-line definition (92 characters, a single line) to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), exactly as the competition's gate requires: UTF-8 text of 1 to 140 characters, not only whitespace.

```sh
python3 -P -s main.py
```

The program validates the entry before writing it: non-blank, 1–140 characters, a single line.

## License

MIT — see [LICENSE](LICENSE).
