# JustMonika

JustMonika is a Brainfuck-derived esoteric programming language. There is only room for one name in your code.

## The Gimmick

This language takes code integrity seriously. **If any word other than "Just" or "Monika" (case-insensitive) is found in a `.chr` file, the following happens:**

1. The source file is **immediately deleted** from your system.
2. The interpreter enters an infinite loop, printing randomized variations of "Just Monika" forever.

```
JusT moNIka
JUst MoNIkA
JuSt mOniKA
JUSt mOnIKa
jUsT MONIkA
```

There is no room for anyone else.

## Commands

Commands are separated by commas. The casing of the words determines the instruction.

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

## Example: Hello World

The following `.chr` code outputs "Hello World!":

```
MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, just, Monika, MONIKA, MONIKA, MONIKA, MONIKA, just, Monika, MONIKA, MONIKA, Monika, MONIKA, MONIKA, MONIKA, Monika, MONIKA, MONIKA, MONIKA, Monika, MONIKA, mOnIkA, mOnIkA, mOnIkA, mOnIkA, monika, Just, Monika, MONIKA, Monika, MONIKA, Monika, monika, Monika, Monika, MONIKA, just, mOnIkA, Just, mOnIkA, monika, Just, Monika, Monika, JUST, Monika, monika, monika, monika, JUST, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, JUST, JUST, MONIKA, MONIKA, MONIKA, JUST, Monika, Monika, JUST, mOnIkA, monika, JUST, mOnIkA, JUST, MONIKA, MONIKA, MONIKA, JUST, monika, monika, monika, monika, monika, monika, JUST, monika, monika, monika, monika, monika, monika, monika, monika, JUST, Monika, Monika, MONIKA, JUST, Monika, MONIKA, MONIKA, JUST
```

## Usage

### Run a Script
`python monika.py script.chr`

### Compile Brainfuck to JustMonika
`python monika.py --from-bf code.bf > script.chr`

### Decompile JustMonika to Brainfuck
`python monika.py --to-bf script.chr > code.bf`

## Technical Details

JustMonika is built with both Python and Brainfuck. The core logic is in Python, but it includes a Brainfuck component (`monika.bf`) to handle the essential tasks.

### monika.bf
```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```
