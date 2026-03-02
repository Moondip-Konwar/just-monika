# JustMonika

JustMonika is an esoteric programming language based on the Brainfuck machine model. It exclusively uses variations of the words "Just" and "Monika".

## Commands

The language uses three-word sequences to represent Brainfuck commands:

| Sequence | Brainfuck | Description |
|----------|-----------|-------------|
| Just Just Just | > | Increment data pointer |
| Just Just Monika | < | Decrement data pointer |
| Just Monika Just | + | Increment byte at pointer |
| Just Monika Monika | - | Decrement byte at pointer |
| Monika Just Just | . | Output byte at pointer |
| Monika Just Monika | , | Input byte at pointer |
| Monika Monika Just | [ | Jump forward if byte is 0 |
| Monika Monika Monika | ] | Jump backward if byte is not 0 |

## Rules

- Any word other than "Just" or "Monika" (case-insensitive) will result in the source file being deleted and "Just Monika" being printed.
- Files must have the .chr extension.

## Usage

Run a script using the provided runner:

python monika.py script.chr

## Sample

Check hello.chr for a Hello World implementation.
