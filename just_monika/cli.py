import sys
from just_monika.lexer import tokenize
from just_monika.interpreter import Interpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python monika.py <file.chr>")
        return

    file_path = sys.argv[1]
    if not file_path.endswith('.chr'):
        print("Just Monika (.chr)")
        return

    commands = tokenize(file_path)
    
    interpreter = Interpreter(commands)
    interpreter.run()

if __name__ == "__main__":
    main()
