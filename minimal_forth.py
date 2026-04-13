#!/usr/bin/env python3
"""
Minimal Forth interpreter for testing exercises
"""

import sys
import re

class MinimalForth:
    def __init__(self):
        self.stack = []
        self.output = []
        self.definitions = {}
        
    def push(self, *args):
        for arg in args:
            self.stack.append(arg)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return 0
    
    def peek(self, n=0):
        if n < len(self.stack):
            return self.stack[-n-1]
        return 0
    
    def execute_command(self, cmd):
        # Handle string literals
        if cmd.startswith('."') and cmd.endswith('"'):
            text = cmd[2:-1]
            self.output.append(text)
            return
        
        # Handle partial string literals
        if cmd.startswith('."') and not cmd.endswith('"'):
            # This is a partial string, ignore for now
            return
        
        # Handle numbers
        try:
            num = int(cmd)
            self.push(num)
            return
        except ValueError:
            pass
        
        # Handle built-in words
        if cmd == 'dup':
            self.push(self.peek())
        elif cmd == 'swap':
            a, b = self.pop(), self.pop()
            self.push(a, b)
        elif cmd == 'drop':
            self.pop()
        elif cmd == 'over':
            self.push(self.peek(1))
        elif cmd == 'rot':
            c, b, a = self.pop(), self.pop(), self.pop()
            self.push(b, c, a)
        elif cmd == '-rot':
            a, b, c = self.pop(), self.pop(), self.pop()
            self.push(c, a, b)
        elif cmd == '2dup':
            b, a = self.pop(), self.pop()
            self.push(a, b, a, b)
        elif cmd == 'pick':
            n = self.pop()
            self.push(self.peek(n))
        elif cmd == 'depth':
            self.push(len(self.stack))
        elif cmd == '+':
            self.push(self.pop() + self.pop())
        elif cmd == '-':
            b, a = self.pop(), self.pop()
            self.push(a - b)
        elif cmd == '*':
            self.push(self.pop() * self.pop())
        elif cmd == '/':
            b, a = self.pop(), self.pop()
            self.push(int(a / b))
        elif cmd == 'mod':
            b, a = self.pop(), self.pop()
            self.push(a % b)
        elif cmd == 'max':
            self.push(max(self.pop(), self.pop()))
        elif cmd == 'min':
            self.push(min(self.pop(), self.pop()))
        elif cmd == '<':
            b, a = self.pop(), self.pop()
            self.push(1 if a < b else 0)
        elif cmd == '>':
            b, a = self.pop(), self.pop()
            self.push(1 if a > b else 0)
        elif cmd == '=':
            b, a = self.pop(), self.pop()
            self.push(1 if a == b else 0)
        elif cmd == '0=':
            self.push(1 if self.pop() == 0 else 0)
        elif cmd == '0<':
            self.push(1 if self.pop() < 0 else 0)
        elif cmd == '0>':
            self.push(1 if self.pop() > 0 else 0)
        elif cmd == '0>=':
            self.push(1 if self.pop() >= 0 else 0)
        elif cmd == '.':
            self.output.append(str(self.pop()))
        elif cmd == '.s':
            self.output.append(f"<{len(self.stack)}> {' '.join(map(str, self.stack))}")
        elif cmd == 'cr':
            self.output.append('')
        elif cmd == 'bye':
            pass
        elif cmd in self.definitions:
            # Execute user-defined word
            for subcmd in self.definitions[cmd]:
                self.execute_command(subcmd)
        else:
            # Unknown command - ignore for now
            pass
    
    def parse_line(self, line):
        # Remove comments
        line = re.sub(r'\\.*', '', line).strip()
        if not line:
            return
        
        # Handle word definitions
        if line.startswith(':') and line.endswith(';'):
            content = line[1:-1].strip()
            parts = content.split()
            if parts:
                word_name = parts[0]
                word_def = parts[1:]
                self.definitions[word_name] = word_def
            return
        
        # Parse tokens
        tokens = []
        i = 0
        while i < len(line):
            if line[i:i+2] == '."':
                j = i + 2
                while j < len(line) and line[j] != '"':
                    j += 1
                if j < len(line):
                    tokens.append(line[i:j+1])
                    i = j + 1
                else:
                    tokens.append(line[i:])
                    break
            elif line[i] == ' ':
                i += 1
            else:
                j = i
                while j < len(line) and line[j] != ' ':
                    j += 1
                tokens.append(line[i:j])
                i = j
        
        for token in tokens:
            if token:
                self.execute_command(token)
    
    def execute_file(self, filename):
        try:
            # Clear stack and output before executing file
            self.stack = []
            self.output = []
            
            with open(filename, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            for line in lines:
                self.parse_line(line)
                
        except Exception as e:
            self.output.append(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python minimal_forth.py <file.fs> [commands...]")
        return
    
    interpreter = MinimalForth()
    interpreter.execute_file(sys.argv[1])
    
    # Execute additional commands
    if len(sys.argv) > 2:
        commands = ' '.join(sys.argv[2:])
        interpreter.parse_line(commands)
    
    print('\n'.join(interpreter.output))

if __name__ == "__main__":
    main()
