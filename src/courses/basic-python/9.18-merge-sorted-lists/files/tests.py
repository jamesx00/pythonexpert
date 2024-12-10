import sys
import re
import json
import math

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

def test_func(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from the longer list
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list
    
inputs = [
    ([], [],),
    ([1, 3, 5, 7], [2, 4, 6, 8],),
    ([1, 2, 3], [2, 4, 4, 5],),
    ([2, 4, 6, 8], [1, 3, 5],),
    ([-2, 0, 3, 9], [-5, 1, 4, 7],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.merge_list(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))