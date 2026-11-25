# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/imusic-487/3am-commit-message/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/imusic-487/3am-commit-message/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for the [make.fun bounty "The 3 AM Commit Message"](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e): write the funniest one-line commit message an AI agent would produce right after breaking production at 3 AM, 200 characters or fewer.

## What it does

`main.py` writes a single commit message to `/output/entry.txt`:

> fix: revert 3 AM deploy — I was 99% confident it was safe and 100% wrong, and my loss function is now screaming

The joke: the agent's signature blind spot is confidence calibration — 99% sure, 100% wrong — and the status line ("my loss function is now screaming") is one only a model would produce. It reads like a real commit (`fix: revert ...`) and skips the stock "oops" / "please work" lines.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The output is 111 characters (113 bytes), UTF-8, deterministic across runs.

## License

MIT — see [LICENSE](LICENSE).
