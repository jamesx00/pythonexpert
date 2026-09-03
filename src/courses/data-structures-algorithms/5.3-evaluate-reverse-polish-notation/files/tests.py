import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(tokens):
    stack = []
    ops = {'+', '-', '*', '/'}
    for tok in tokens:
        if tok in ops:
            b = stack.pop()
            a = stack.pop()
            if tok == '+':
                stack.append(a + b)
            elif tok == '-':
                stack.append(a - b)
            elif tok == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[-1]

inputs = [
    (["2", "1", "+", "3", "*"],),
    (["4", "13", "5", "/", "+"],),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],),
    (["5"],),
    (["7", "2", "-"],),
    (["6", "-3", "/"],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.evaluate_rpn(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
