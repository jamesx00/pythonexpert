import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_build_tree_from_traversals(preorder, inorder):
    def build(pre, ino):
        if not pre:
            return None
        root_val = pre[0]
        root = main.TreeNode(root_val)
        idx = ino.index(root_val)
        left_ino = ino[:idx]
        right_ino = ino[idx + 1:]
        left_pre = pre[1:1 + len(left_ino)]
        right_pre = pre[1 + len(left_ino):]
        root.left = build(left_pre, left_ino)
        root.right = build(right_pre, right_ino)
        return root

    return main.tree_to_list(build(preorder, inorder))

inputs = [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
    ([-1], [-1]),
    ([], []),
    ([1, 2, 3], [3, 2, 1]),
    ([1, 2, 3], [1, 2, 3]),
    ([5, 3, 1, 4, 8, 7, 9], [1, 3, 4, 5, 7, 8, 9]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_build_tree_from_traversals(*i)
        root = main.build_tree_from_traversals(*i)
        assert main.tree_to_list(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
