import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_invert_tree(values):
    root = main.build_tree(values)

    def invert(node):
        if node is None:
            return None
        node.left, node.right = invert(node.right), invert(node.left)
        return node

    return main.tree_to_list(invert(root))

inputs = [
    ([4, 2, 7, 1, 3, 6, 9],),
    ([1, 2],),
    ([1, None, 2],),
    ([],),
    ([5],),
    ([3, 9, 20, None, None, 15, 7],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_invert_tree(*i)
        root = main.build_tree(*i)
        assert main.tree_to_list(main.invert_tree(root)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
