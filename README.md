# tuMachine

A library for generating Turing machine code: you chain ready-made blocks (move, copy, slice a number, …) and get a transition table for any number base from 2 to 36.

The blocks were written as building pieces for a Turing machine that divides numbers with remainder. The approach is my own rather than a standard step-by-step algorithm; only the divisibility rules are borrowed (for example, `SliceNumber` is meant for the divisibility rule for 11). Division itself was never finished.

> **Note:** this project is no longer actively maintained. Some classes are unfinished or broken — see the [API](#api) section.

## Requirements

Python 3.12 or newer.

## Installation

The package is not published on PyPI. Install it directly from GitHub:

```
pip install git+https://github.com/kontar0/tuMachine-proj.git
```

Or clone the repository and install it locally:

```
git clone https://github.com/kontar0/tuMachine-proj.git
cd tuMachine-proj
pip install .
```

## Usage

You build a program out of functions (blocks), pass them to `Constructor` together with the number base, and write the resulting transition table to a file:

```python
from tuMachine import *

left_two_numbers = MoveThrought(2, 0)
copy_num = CopyThrought(2, 1, 1)

c = Constructor([left_two_numbers, copy_num], 2)
c.build('tuCode.txt')
```

The tape holds numbers separated by single blank cells, and the head starts on the blank cell right after the last number. For the tape `101 11 1` this program does the following:

1. `MoveThrought(2, 0)` moves the head left past two numbers, so it stops on the blank between `101` and `11`.
2. `CopyThrought(2, 1, 1)` copies the number to the right of the head (`11`) to the end of the tape: `101 11 1 11`.

The second argument of `Constructor` is the number base: from 2 to 36. Digits `0-9` and then letters `A-Z` are used as the alphabet.

### Output format

`build()` writes one transition per line:

```
state,symbol,action,next_state
```

- `state`, `next_state` — state names;
- `symbol` — the symbol under the head (a space means a blank cell);
- `action` — `<` move left, `>` move right, `=` stay, or a symbol to write into the current cell.

## API

Directions are passed as integers: `0` — left, `1` — right.

| Class | Description | Known issues |
|---|---|---|
| `Constructor(functions, power)` | Chains the functions into one program for base `power`; `build(filename)` writes it to a file. | — |
| `Function` | Base class for all blocks. | — |
| `MoveThrought(elements, direction)` | Moves the head past `elements` numbers in `direction`. | — |
| `CopyThrought(elements, directionFrom, directionTo)` | Copies the number on the `directionFrom` side of the head and writes the copy `elements` numbers away in `directionTo`. | — |
| `CopySymbol(elements, direction)` | Helper used by the copying blocks: carries digits one by one `elements` numbers away. | — |
| `SliceNumber(elements, directionFrom, directionTo)` | Splits a number into its odd- and even-position digits (counted from the side nearest the head) and copies them `elements` numbers away in `directionTo`. | — |
| `CopyThroughtBeforeRight(placeStopSymbol, elements, directionFrom, directionTo)` | Copies a sequence of symbols before the stop symbol (`$`). | broken: the last transition gets an invalid state name |
| `DeleteWordBeforeSymbol()` | Deletes the word before the special symbol (`$`). | broken: the last transition gets an invalid state name |
| `Subtraction()` | Subtraction. | unfinished: raises `TypeError` |

All blocks also accept the optional arguments `rank=4` (length of the generated state names) and `specSymbol="$"`.

## License

MIT — see [LICENSE](LICENSE).
