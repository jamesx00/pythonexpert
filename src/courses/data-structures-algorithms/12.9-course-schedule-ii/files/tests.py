import sys
import json
from collections import defaultdict

from unittest.mock import patch
patch('builtins.print').start()

import main

def is_feasible(num_courses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = {}

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

def check_order(num_courses, prerequisites, order):
    if sorted(order) != list(range(num_courses)):
        return False
    position = {course: i for i, course in enumerate(order)}
    for course, prereq in prerequisites:
        if position[prereq] >= position[course]:
            return False
    return True

inputs = [
    (3, [[1, 0], [2, 1]]),
    (2, [[1, 0]]),
    (2, [[1, 0], [0, 1]]),
    (1, []),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    (3, []),
]

results = {}

for index, i in enumerate(inputs):
    try:
        feasible = is_feasible(*i)
        student_result = main.find_order(*i)
        if feasible:
            ok = check_order(i[0], i[1], student_result)
        else:
            ok = (student_result == [])
        assert ok
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
