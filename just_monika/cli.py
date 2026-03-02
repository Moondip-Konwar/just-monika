import sys
from just_monika.lexer import tokenize, get_commands
from just_monika.interpreter import Interpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python monika.py <file.chr>")
        return

    file_path = sys.argv[1]
    if not file_path.endswith('.chr'):
        print("Just Monika (.chr)")
        return

    tokens = tokenize(file_path)
    commands = get_commands(tokens)
    
    interpreter = Interpreter(commands)
    interpreter.run()

if __name__ == "__main__":
    main()
