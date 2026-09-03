import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_good_nodes(values):
    root = main.build_tree(values)
    count = [0]

    def dfs(node, max_so_far):
        if node is None:
            return
        if node.val >= max_so_far:
            count[0] += 1
            max_so_far = node.val
        dfs(node.left, max_so_far)
        dfs(node.right, max_so_far)

    dfs(root, float('-inf'))
    return count[0]

inputs = [
    ([3, 1, 4, 3, None, 1, 5],),
    ([3, 3, None, 4, 2],),
    ([1],),
    ([],),
    ([5, 4, 3, 2, 1],),
    ([1, 2, 3, 4, 5, 6, 7],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_good_nodes(*i)
        root = main.build_tree(*i)
        assert main.good_nodes(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
