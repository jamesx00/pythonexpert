import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_max_path_sum(values):
    root = main.build_tree(values)
    best = [float('-inf')]

    def dfs(node):
        if node is None:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        best[0] = max(best[0], node.val + left + right)
        return node.val + max(left, right)

    dfs(root)
    return best[0]

inputs = [
    ([-10, 9, 20, None, None, 15, 7],),
    ([1, 2, 3],),
    ([-3],),
    ([2, -1],),
    ([-1, -2, -3],),
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_max_path_sum(*i)
        root = main.build_tree(*i)
        assert main.max_path_sum(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
