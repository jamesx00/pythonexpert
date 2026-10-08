import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

inputs = [
    ([1, 2, 3, None, None, 4, 5],),
    ([],),
    ([1],),
    ([1, 2],),
    ([5, 4, 7, 3, None, 2, None, -1, None, 9],),
    ([1, None, 2, None, 3, None, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        values = i[0]
        root = main.build_tree(values)
        expected = main.tree_to_list(root)
        data = main.serialize(root)
        rebuilt = main.deserialize(data)
        assert main.tree_to_list(rebuilt) == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
