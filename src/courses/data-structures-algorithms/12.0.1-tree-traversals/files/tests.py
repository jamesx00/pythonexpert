import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def preorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result


def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


def postorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result

def check(fn, values, *rest):
    return fn(build_tree(values), *rest)

cases = [
    ('preorder', ([1, 2, 3, 4, 5],)),
    ('inorder', ([1, 2, 3, 4, 5],)),
    ('postorder', ([1, 2, 3, 4, 5],)),
    ('inorder', ([4, 2, 6, 1, 3, 5, 7],)),
    ('preorder', ([],)),
    ('postorder', ([1, None, 2, None, 3],)),
    ('inorder', ([1, None, 2, 3],)),
]

results = {}

for index, (name, args) in enumerate(cases):
    try:
        expected = check(globals()[name], *copy.deepcopy(args))
        assert check(getattr(main, name), *copy.deepcopy(args)) == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
