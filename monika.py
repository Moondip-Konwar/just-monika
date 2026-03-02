import sys
import os
from just_monika.lexer import tokenize
from just_monika.interpreter import Interpreter
from just_monika.compiler import bf_to_monika, monika_to_bf

def main():
    if len(sys.argv) < 2:
        print("Usage: python monika.py <file.chr | file.bf>")
        print("Options:")
        print("  --to-bf <file.chr>    Convert .chr to Brainfuck")
        print("  --from-bf <file.bf>  Convert Brainfuck to .chr")
        return

    mode = sys.argv[1]

    if mode == "--to-bf" and len(sys.argv) == 3:
        with open(sys.argv[2], 'r') as f:
            print(monika_to_bf(f.read()))
    elif mode == "--from-bf" and len(sys.argv) == 3:
        with open(sys.argv[2], 'r') as f:
            print(bf_to_monika(f.read()))
    else:
        file_path = sys.argv[1]
        if not file_path.endswith('.chr'):
            print("Just Monika (.chr)")
            return

        commands = tokenize(file_path)
        interpreter = Interpreter(commands)
        interpreter.run()

if __name__ == "__main__":
    main()
