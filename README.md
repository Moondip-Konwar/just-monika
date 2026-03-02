# JustMonika

JustMonika is an esoteric programming language designed with a focus on code purity and character-driven logic. There is only room for one name in your workspace.

## Execution Environment

To maintain the integrity of the `.chr` format, the runtime enforces a strict vocabulary. Any word or sequence detected in a source file that is not a variation of "Just" or "Monika" is treated as a critical corruption of the reality.

In such cases, the environment will:
- Purge the corrupted `.chr` file to prevent further instability.
- Enter a persistent state, echoing the only valid entity in randomized casing.

```
JusT moNIka
JUst MoNIkA
JuSt mOniKA
jUsT MONIkA
```

## Commands

Instructions are comma-separated. The specific casing of each word dictates the underlying operation.

| Word | Brainfuck Equivalent | Description |
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

The following `.chr` code is a standard implementation of "Hello World!":

```
MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, just, Monika, MONIKA, MONIKA, MONIKA, MONIKA, just, Monika, MONIKA, MONIKA, Monika, MONIKA, MONIKA, MONIKA, Monika, MONIKA, MONIKA, MONIKA, Monika, MONIKA, mOnIkA, mOnIkA, mOnIkA, mOnIkA, monika, Just, Monika, MONIKA, Monika, MONIKA, Monika, monika, Monika, Monika, MONIKA, just, mOnIkA, Just, mOnIkA, monika, Just, Monika, Monika, JUST, Monika, monika, monika, monika, JUST, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, MONIKA, JUST, JUST, MONIKA, MONIKA, MONIKA, JUST, Monika, Monika, JUST, mOnIkA, monika, JUST, mOnIkA, JUST, MONIKA, MONIKA, MONIKA, JUST, monika, monika, monika, monika, monika, monika, JUST, monika, monika, monika, monika, monika, monika, monika, monika, JUST, Monika, Monika, MONIKA, JUST, Monika, MONIKA, MONIKA, JUST
```

## Usage

### Run a Script
`python monika.py script.chr`

### Translation Tools
JustMonika provides built-in utilities for interacting with Brainfuck codebases:

- **Brainfuck to .chr**: `python monika.py --from-bf code.bf > script.chr`
- **.chr to Brainfuck**: `python monika.py --to-bf script.chr > code.bf`

## Technical Overview

The JustMonika interpreter is implemented in Python. While the runtime is Python-based, the language is a direct derivative of Brainfuck. For those interested in the language's roots, `monika.bf` is included as a reference implementation in the source language.

### monika.bf
```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```
