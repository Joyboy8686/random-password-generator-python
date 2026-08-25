# Random Password Generator (CLI)

A command-line password generator built in Python that creates a random password
from a mix of uppercase letters, lowercase letters, numbers, and symbols, with
input validation on the desired length.

## Features
- Combines uppercase, lowercase, numbers, and symbols into one character pool
- Generates a password using random selection **with repetition allowed**
  (matches how real-world passwords work — characters can repeat)
- Validates length input: must be a whole number between 1 and 16
- Loops on invalid input (non-numeric, zero, negative, or too large) instead of crashing

## Concepts practiced
- The `random` module — specifically `random.choices()` vs `random.sample()`,
  and why `choices()` (allows repetition) is the correct tool for password
  generation rather than `sample()` (no repetition, which artificially shrinks
  the pool of possible passwords and reduces randomness)
- String concatenation to build a character pool
- Avoiding Python built-in/keyword names (`all`, `pass`) as variable names
- `while True` + `try/except ValueError` for robust input validation, reused
  from an earlier project
- Keyword arguments (`k=length`) vs positional arguments

## How to run
```bash
python randompassgene.py
```

## Example
```
RANDOM PASSWORD GENERATOR

Enter Desired Length For Password : 12
aG7$kLp9@qXz
```

## What I learned
This project builds on the input-validation pattern from my Contact Book project.
The interesting part was realizing `random.sample()` — which felt like the obvious
choice at first — actually forces every character in the password to be unique,
which isn't how real passwords work and can even crash if the requested length
is longer than the character pool. Switching to `random.choices()` fixed both
the correctness and the security reasoning behind it.
