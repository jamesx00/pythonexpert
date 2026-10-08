import sys
import json
import copy
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def min_depth(root):
    if not root:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

def check(fn, values, *rest):
    return fn(build_tree(values), *rest)

cases = [
    ('min_depth', ([3, 9, 20, None, None, 15, 7],)),
    ('min_depth', ([],)),
    ('min_depth', ([1],)),
    ('min_depth', ([2, None, 3, None, 4, None, 5, None, 6],)),
    ('min_depth', ([1, 2, 3, 4, 5],)),
    ('min_depth', ([1, 2, 3, 4, None, None, 5, 6],)),
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
