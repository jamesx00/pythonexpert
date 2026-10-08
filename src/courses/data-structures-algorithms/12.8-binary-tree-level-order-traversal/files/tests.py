import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_level_order(values):
    root = main.build_tree(values)
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            level.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        result.append(level)
        queue = next_queue
    return result

inputs = [
    ([3, 9, 20, None, None, 15, 7],),
    ([],),
    ([1],),
    ([1, 2, 3, 4, 5, 6, 7],),
    ([1, None, 2, None, 3],),
    ([1, 2, None, 3],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_level_order(*i)
        root = main.build_tree(*i)
        assert main.level_order(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
