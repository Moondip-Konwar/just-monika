# JustMonika

JustMonika is an esoteric programming language based on the Brainfuck machine model. It exclusively uses the words "Just" and "Monika". Commands are determined by the specific casing of these words.

## Commands

Commands are separated by commas. Monika variations are mapped to the most common operations.

| Word | Brainfuck | Description |
|------|-----------|-------------|
| MONIKA | + | Increment byte at pointer |
| monika | - | Decrement byte at pointer |
| Monika | > | Increment data pointer |
| mOnIkA | < | Decrement data pointer |
| JUST | . | Output byte at pointer |
| jUsT | , | Input byte at pointer |
| just | [ | Jump forward if byte is 0 |
| Just | ] | Jump backward if byte is not 0 |

## Rules

- Any word other than "Just" or "Monika" (case-insensitive) will result in the source file being deleted.
- If an invalid word is encountered, the program will enter an infinite loop printing "Just Monika" in randomized casing.
- Files must have the .chr extension.

## Usage

Run a script using the provided runner:

```python3
python3 monika.py script.chr
```

## Sample
Printing "Hello World!" in Just Monika:
```
MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, just, Monika, MONIKA, MONIKA, MONIKA, MONIKA, just, Monika, MONIKA, MONIKA, Monika, MONIKA, MONIKA, MONIKA, Monika, MONIKA, MONIKA, MONIKA, Monika, MONIKA, mOnIkA, mOnIkA, mOnIkA, mOnIkA, monika, Just, Monika, MONIKA, Monika, MONIKA, Monika, monika, Monika, Monika, MONIKA, just, mOnIkA, Just, mOnIkA, monika, Just, Monika, Monika, JUST, Monika, monika, monika, monika, JUST, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, JUST, JUST, MONIKA, MONIKA, MONIKA, JUST, Monika, Monika, JUST, mOnIkA, monika, JUST, mOnIkA, JUST, MONIKA, MONIKA, MONIKA, JUST, monika, monika, monika, monika, monika, monika, JUST, monika, monika, monika, monika, monika, monika, monika, monika, JUST, Monika, Monika, MONIKA, JUST, Monika, MONIKA, MONIKA, JUST
```
