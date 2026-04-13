#!/usr/bin/env python3
"""
Simple Forth interpreter for testing purposes
"""

import sys
import re
from typing import List

class ForthInterpreter:
    def __init__(self):
        self.stack = []
        self.output = []
        self.words = {}
        self.define_builtin_words()
    
    def define_builtin_words(self):
        # Stack operations
        self.words['dup'] = lambda: self.push(self.peek())
        self.words['swap'] = lambda: self.push(self.pop(1), self.pop())
        self.words['drop'] = lambda: self.pop()
        self.words['over'] = lambda: self.push(self.peek(1))
        self.words['rot'] = lambda: self.push(self.pop(2), self.pop(1), self.pop())
        self.words['-rot'] = lambda: self.push(self.pop(), self.pop(2), self.pop(1))
        self.words['2dup'] = lambda: self.push(self.peek(1), self.peek(1))
        self.words['pick'] = lambda: self.push(self.peek(self.pop()))
        self.words['depth'] = lambda: self.push(len(self.stack))
        
        # Math operations
        self.words['+'] = lambda: self.push(self.pop() + self.pop())
        self.words['-'] = lambda: self.push(self.pop(1) - self.pop())
        self.words['*'] = lambda: self.push(self.pop() * self.pop())
        self.words['/'] = lambda: self.push(int(self.pop(1) / self.pop()))
        self.words['mod'] = lambda: self.push(self.pop(1) % self.pop())
        self.words['max'] = lambda: self.push(max(self.pop(1), self.pop()))
        self.words['min'] = lambda: self.push(min(self.pop(1), self.pop()))
        self.words['<'] = lambda: self.push(1 if self.pop(1) < self.pop() else 0)
        self.words['>'] = lambda: self.push(1 if self.pop(1) > self.pop() else 0)
        self.words['='] = lambda: self.push(1 if self.pop(1) == self.pop() else 0)
        self.words['0='] = lambda: self.push(1 if self.pop() == 0 else 0)
        self.words['0<'] = lambda: self.push(1 if self.pop() < 0 else 0)
        self.words['0>'] = lambda: self.push(1 if self.pop() > 0 else 0)
        self.words['0>='] = lambda: self.push(1 if self.pop() >= 0 else 0)
        
        # Output operations
        self.words['.'] = lambda: self.output.append(str(self.pop()))
        self.words['.s'] = lambda: self.output.append(f"<{len(self.stack)}> {' '.join(map(str, self.stack))}")
        self.words['cr'] = lambda: self.output.append('')
        
        # String output
        self.words['."'] = self.handle_string_literal
        
        # Control flow (simplified)
        self.words['if'] = self.handle_if
        self.words['then'] = lambda: None  # placeholder
        self.words['else'] = lambda: None  # placeholder
        self.words['do'] = self.handle_do
        self.words['loop'] = lambda: None  # placeholder
        self.words['begin'] = lambda: None  # placeholder
        self.words['until'] = lambda: None  # placeholder
        self.words['while'] = lambda: None  # placeholder
        self.words['repeat'] = lambda: None  # placeholder
        self.words['i'] = self.handle_i
        self.words['exit'] = lambda: None  # placeholder
        
        # Word definition
        self.words[':'] = self.handle_colon
        self.words[';'] = self.handle_semicolon
        
        # Misc
        self.words['bye'] = lambda: None
    
    def push(self, *args):
        for arg in args:
            self.stack.append(arg)
    
    def pop(self, n=0):
        if not self.stack:
            return 0
        if n == 0:
            return self.stack.pop()
        else:
            idx = -n-1
            if idx >= -len(self.stack):
                return self.stack.pop(idx)
            return 0
    
    def peek(self, n=0):
        if n >= len(self.stack):
            return 0
        return self.stack[-n-1]
    
    def handle_string_literal(self):
        # This is a simplified implementation
        # In real Forth, ." would be handled during parsing
        pass
    
    def handle_if(self):
        # Simplified if handling
        pass
    
    def handle_do(self):
        # Simplified do...loop handling
        pass
    
    def handle_i(self):
        # Simplified loop counter
        pass
    
    def handle_colon(self):
        # Simplified word definition
        pass
    
    def handle_semicolon(self):
        # Simplified word definition end
        pass
    
    def parse_line(self, line):
        # Remove comments
        line = re.sub(r'\\.*', '', line).strip()
        if not line:
            return
        
        # Handle string literals
        parts = []
        i = 0
        while i < len(line):
            if line[i:i+2] == '."':
                # Find closing quote
                j = i + 2
                while j < len(line) and line[j] != '"':
                    j += 1
                if j < len(line):
                    parts.append(line[i+2:j])
                    i = j + 1
                else:
                    parts.append(line[i+2:])
                    break
            else:
                # Find next space
                j = i
                while j < len(line) and line[j] != ' ':
                    j += 1
                parts.append(line[i:j])
                i = j + 1
        
        for token in parts:
            if token == '':
                continue
            
            # Check if it's a number
            try:
                num = int(token)
                self.push(num)
            except ValueError:
                # Check if it's a word
                if token in self.words:
                    self.words[token]()
                else:
                    # Try to execute as user-defined word
                    pass
    
    def execute_file(self, filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            for line in lines:
                self.parse_line(line)
            
        except Exception as e:
            self.output.append(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python simple_forth.py <file.fs> [commands...]")
        return
    
    interpreter = ForthInterpreter()
    
    # Execute file first
    interpreter.execute_file(sys.argv[1])
    
    # Execute additional commands if provided
    if len(sys.argv) > 2:
        commands = ' '.join(sys.argv[2:])
        interpreter.parse_line(commands)
    
    print('\n'.join(interpreter.output))

if __name__ == "__main__":
    main()
