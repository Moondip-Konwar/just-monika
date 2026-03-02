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

python monika.py script.chr

## Sample

Check hello.chr for a Hello World implementation using comma-separated casing commands.
