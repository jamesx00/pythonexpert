import sys
import json
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main

def get_constraints(words):
    letters = set()
    for w in words:
        letters.update(w)
    edges = set()
    prefix_invalid = False
    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))
        found = False
        for i in range(min_len):
            if w1[i] != w2[i]:
                edges.add((w1[i], w2[i]))
                found = True
                break
        if not found and len(w1) > len(w2):
            prefix_invalid = True
    return letters, edges, prefix_invalid

def has_cycle(letters, edges):
    graph = {c: [] for c in letters}
    indegree = {c: 0 for c in letters}
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1
    q = deque([c for c in letters if indegree[c] == 0])
    visited_count = 0
    while q:
        c = q.popleft()
        visited_count += 1
        for nxt in graph[c]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return visited_count != len(letters)

def is_valid_order(words, order):
    letters, edges, prefix_invalid = get_constraints(words)
    if prefix_invalid or has_cycle(letters, edges):
        return order == ""
    if not order or sorted(order) != sorted(letters):
        return False
    pos = {c: i for i, c in enumerate(order)}
    for a, b in edges:
        if pos[a] >= pos[b]:
            return False
    return True

inputs = [
    (["z", "x"],),
    (["z", "x", "z"],),
    (["abc", "ab"],),
    (["ac", "ab", "zc", "zb"],),
    (["wrt", "wrf", "er", "ett", "rftt"],),
    (["abc", "abd", "abe"],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        student_result = main.alien_order(*i)
        assert is_valid_order(i[0], student_result)
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
