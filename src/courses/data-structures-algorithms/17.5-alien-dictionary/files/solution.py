from collections import deque


def alien_order(words):
    letters = set()
    for w in words:
        letters.update(w)

    graph = {c: [] for c in letters}
    indegree = {c: 0 for c in letters}

    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))
        found = False
        for i in range(min_len):
            if w1[i] != w2[i]:
                graph[w1[i]].append(w2[i])
                indegree[w2[i]] += 1
                found = True
                break
        if not found and len(w1) > len(w2):
            return ""

    q = deque([c for c in letters if indegree[c] == 0])
    order = []

    while q:
        c = q.popleft()
        order.append(c)
        for nxt in graph[c]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    if len(order) != len(letters):
        return ""

    return "".join(order)
