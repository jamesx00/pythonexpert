import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_right_side_view(values):
    root = main.build_tree(values)
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        next_queue = []
        for index, node in enumerate(queue):
            if index == len(queue) - 1:
                result.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    return result

inputs = [
    ([1, 2, 3, None, 5, None, 4],),
    ([1, None, 3],),
    ([],),
    ([1],),
    ([1, 2, 3, 4],),
    ([1, 2, 3, 4, None, None, 5],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_right_side_view(*i)
        root = main.build_tree(*i)
        assert main.right_side_view(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
