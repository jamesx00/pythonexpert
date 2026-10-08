import sys
import json
from collections import defaultdict

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = {}  # 0 = visiting, 1 = done

    def dfs(node):
        if state.get(node) == 0:
            return False
        if state.get(node) == 1:
            return True
        state[node] = 0
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        state[node] = 1
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True

inputs = [
    (2, [[1, 0]]),
    (2, [[1, 0], [0, 1]]),
    (4, [[1, 0], [2, 1], [3, 2]]),
    (3, [[0, 1], [1, 2], [2, 0]]),
    (1, []),
    (5, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    (2, []),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_can_finish(*i)
        assert main.can_finish(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
