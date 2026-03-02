import sys

class Interpreter:
    def __init__(self, commands):
        self.commands = commands
        self.tape = [0] * 30000
        self.ptr = 0
        self.pc = 0
        self.loop_map = self._preprocess_loops()

    def _preprocess_loops(self):
        stack = []
        mapping = {}
        for i, cmd in enumerate(self.commands):
            if cmd == '[':
                stack.append(i)
            elif cmd == ']':
                start = stack.pop()
                mapping[start] = i
                mapping[i] = start
        return mapping

    def run(self):
        while self.pc < len(self.commands):
            cmd = self.commands[self.pc]
            if cmd == '>':
                self.ptr += 1
            elif cmd == '<':
                self.ptr -= 1
            elif cmd == '+':
                self.tape[self.ptr] = (self.tape[self.ptr] + 1) % 256
            elif cmd == '-':
                self.tape[self.ptr] = (self.tape[self.ptr] - 1) % 256
            elif cmd == '.':
                sys.stdout.write(chr(self.tape[self.ptr]))
                sys.stdout.flush()
            elif cmd == ',':
                char = sys.stdin.read(1)
                self.tape[self.ptr] = ord(char) if char else 0
            elif cmd == '[':
                if self.tape[self.ptr] == 0:
                    self.pc = self.loop_map[self.pc]
            elif cmd == ']':
                if self.tape[self.ptr] != 0:
                    self.pc = self.loop_map[self.pc]
            self.pc += 1
