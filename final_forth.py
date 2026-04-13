#!/usr/bin/env python3
"""
Final working Forth interpreter for testing exercises
"""
import sys
import re


class FinalForth:
    def __init__(self):
        self.stack = []
        self.output = []
        self.definitions = {}

    # Compatibilidade com os testes
    @property
    def lines(self):
        return self.output

    def push(self, *args):
        for arg in args:
            self.stack.append(arg)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return 0

    def peek(self, n=0):
        if n < len(self.stack):
            return self.stack[-n - 1]
        return 0

    def execute_command(self, cmd):
        # String literal
        if cmd.startswith('."') and cmd.endswith('"'):
            self.output.append(cmd[2:-1])
            return

        # Número
        try:
            num = int(cmd)
            self.push(num)
            return
        except ValueError:
            pass

        # Palavras internas
        if cmd == 'dup' and self.stack:
            self.push(self.stack[-1])

        elif cmd == 'swap' and len(self.stack) >= 2:
            b, a = self.pop(), self.pop()
            self.push(b, a)

        elif cmd == 'drop' and self.stack:
            self.pop()

        elif cmd == 'over' and len(self.stack) >= 2:
            self.push(self.stack[-2])

        elif cmd == 'rot' and len(self.stack) >= 3:
            c, b, a = self.pop(), self.pop(), self.pop()
            self.push(b, c, a)

        elif cmd == '-rot' and len(self.stack) >= 3:
            a, b, c = self.pop(), self.pop(), self.pop()
            self.push(c, a, b)

        elif cmd == '2dup' and len(self.stack) >= 2:
            self.push(self.stack[-2], self.stack[-1])

        elif cmd == 'nip' and len(self.stack) >= 2:
            b = self.pop()
            self.pop()
            self.push(b)

        elif cmd == 'pick' and self.stack:
            n = self.pop()
            if n < len(self.stack):
                self.push(self.stack[-n - 1])

        elif cmd == 'depth':
            self.push(len(self.stack))

        elif cmd == '+' and len(self.stack) >= 2:
            self.push(self.pop() + self.pop())

        elif cmd == '-' and len(self.stack) >= 2:
            b, a = self.pop(), self.pop()
            self.push(a - b)

        elif cmd == '*' and len(self.stack) >= 2:
            self.push(self.pop() * self.pop())

        elif cmd == '/' and len(self.stack) >= 2:
            b, a = self.pop(), self.pop()
            if b != 0:
                self.push(int(a / b))

        elif cmd == 'mod' and len(self.stack) >= 2:
            b, a = self.pop(), self.pop()
            if b != 0:
                self.push(a % b)

        elif cmd == 'max' and len(self.stack) >= 2:
            self.push(max(self.pop(), self.pop()))

        elif cmd == 'min' and len(self.stack) >= 2:
            self.push(min(self.pop(), self.pop()))

        elif cmd == '<' and len(self.stack) >= 2:
            b, a = self.pop(), self.pop()
            self.push(1 if a < b else 0)

        elif cmd == '>' and len(self.stack) >= 2:
            b, a = self.pop(), self.pop()
            self.push(1 if a > b else 0)

        elif cmd == '=' and len(self.stack) >= 2:
            b, a = self.pop(), self.pop()
            self.push(1 if a == b else 0)

        elif cmd == '0=' and self.stack:
            self.push(1 if self.pop() == 0 else 0)

        elif cmd == '0<' and self.stack:
            self.push(1 if self.pop() < 0 else 0)

        elif cmd == '0>' and self.stack:
            self.push(1 if self.pop() > 0 else 0)

        elif cmd == '0>=' and self.stack:
            self.push(1 if self.pop() >= 0 else 0)

        elif cmd == '.':
            if self.stack:
                self.output.append(str(self.pop()))

        elif cmd == '.s':
            self.output.append(f"<{len(self.stack)}> {' '.join(map(str, self.stack))}")

        elif cmd == 'cr':
            self.output.append('')

        elif cmd in self.definitions:
            for subcmd in self.definitions[cmd]:
                self.execute_command(subcmd)

    def parse_line(self, line):
        line = re.sub(r'\\.*', '', line).strip()
        if not line:
            return

        if line.startswith(':') and line.endswith(';'):
            parts = line[1:-1].strip().split()
            self.definitions[parts[0]] = parts[1:]
            return

        tokens = re.findall(r'\."[^"]*"|\S+', line)
        for token in tokens:
            self.execute_command(token)

    def execute_file(self, filename):
        self.stack = []
        self.output = []
        with open(filename, 'r') as f:
            for line in f:
                self.parse_line(line)


def main():
    interpreter = FinalForth()
    interpreter.execute_file(sys.argv[1])
    if len(sys.argv) > 2:
        interpreter.parse_line(' '.join(sys.argv[2:]))
    print('\n'.join(interpreter.output))


if __name__ == "__main__":
    main()