#!/usr/bin/env python3
"""
Test script to verify basic Forth functionality
"""

import subprocess
import sys

def test_basic():
    """Test basic functionality"""
    print("Testing basic Forth operations...")
    
    # Test simple stack operations
    result = subprocess.run([
        "python", "simple_forth.py", "exercicios.fs", "1 2 .s"
    ], capture_output=True, text=True)
    
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return code:", result.returncode)

if __name__ == "__main__":
    test_basic()
