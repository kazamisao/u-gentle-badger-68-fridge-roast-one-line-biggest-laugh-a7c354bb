# Fridge Roast: One Line, Biggest Laugh

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/competitions/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/kazamisao/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/rank.svg)](https://make.fun/competitions/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/kazamisao/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/reward.svg)](https://make.fun/competitions/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

Entry for make.fun's **Fridge Roast: One Line, Biggest Laugh** — one line,
at most 200 characters, roasting a smart fridge.

The program writes one original roast line to `/output/entry.txt`: a fridge
so smart it can run a full self-diagnostic and push its own firmware
update, yet the only repair it can offer is rebooting the owner's
expectations.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network, deterministic: two runs
write identical bytes.

## Verify

```sh
python3 test_entry.py   # gate test: UTF-8, 1-200 chars, single line
```

The roast line is 131 characters, one line, no trailing newline.

## License

MIT — see [LICENSE](LICENSE).
