from collections import defaultdict

def find_order(num_courses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = {}  # 0 = visiting, 1 = done
    order = []

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
        order.append(node)
        return True

    for course in range(num_courses):
        if not dfs(course):
            return []
    return order
