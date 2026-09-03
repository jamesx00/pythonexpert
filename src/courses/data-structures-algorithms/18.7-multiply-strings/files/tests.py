import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            d1 = int(num1[i])
            d2 = int(num2[j])
            pos_low = i + j + 1
            pos_high = i + j
            total = d1 * d2 + result[pos_low]
            result[pos_low] = total % 10
            result[pos_high] += total // 10
    digits = ''.join(map(str, result)).lstrip('0')
    return digits if digits else "0"

inputs = [
    ("23", "45"),
    ("2", "3"),
    ("0", "52"),
    ("123", "456"),
    ("999", "999"),
    ("0", "0"),
    ("100", "10"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.multiply(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
