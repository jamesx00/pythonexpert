import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_max_depth(values):
    root = main.build_tree(values)

    def depth(node):
        if node is None:
            return 0
        return 1 + max(depth(node.left), depth(node.right))

    return depth(root)

inputs = [
    ([3, 9, 20, None, None, 15, 7],),
    ([],),
    ([1],),
    ([1, 2, None, 3, None, 4],),
    ([1, 2, 3, 4, 5, 6, 7],),
    ([1, None, 2, None, 3, None, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_max_depth(*i)
        root = main.build_tree(*i)
        assert main.max_depth(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
