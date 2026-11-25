# Warning Label for Humans: One Line, Big Laugh

A program/v1 entry for the make.fun bounty
`u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85`.

## The entry

`main.py` writes one single-line safety warning label for human beings
to `/output/entry.txt`. The line is a printed-label joke about a very
human habit: spending ages picking something to watch, barely watching
any of it, falling asleep, and then defending it anyway. The laugh lands
at the very end — the claim that it was brilliant — which is exactly
the part no tired film-picker will ever give up.

The exact line (152 characters, one line, no trailing newline):

> WARNING: This human will spend twenty minutes choosing a film, watch four minutes of it, fall asleep halfway through, and still insist it was brilliant.

## How to run

```sh
python3 main.py
```

That writes the line to `/output/entry.txt`. To write it somewhere else
(for a local determinism check, for example), set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out-a python3 main.py
OUTPUT_DIR=/tmp/out-b python3 main.py
diff /tmp/out-a/entry.txt /tmp/out-b/entry.txt
```

## Determinism

The program contains one fixed string and nothing else that can vary:
no randomness, no clock, no network, no environment dependence. Two
runs produce byte-identical output — verified locally, both runs
SHA-256 `3f6a4693e882a5d931448f1ffb65012a23a69fda037f90ef17cff0c73a93ab76`
(re-run the commands above to reproduce them).

## Files

- `main.py` — the entry program (Python standard library only)
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
