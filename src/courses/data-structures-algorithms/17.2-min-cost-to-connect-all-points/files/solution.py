def min_cost_connect_points(points):
    n = len(points)
    in_tree = [False] * n
    # best[v]: cheapest edge from the tree to point v found so far
    best = [float("inf")] * n
    best[0] = 0
    total = 0

    for _ in range(n):
        u = -1
        for v in range(n):
            if not in_tree[v] and (u == -1 or best[v] < best[u]):
                u = v
        in_tree[u] = True
        total += best[u]
        ux, uy = points[u]
        for v in range(n):
            if not in_tree[v]:
                d = abs(ux - points[v][0]) + abs(uy - points[v][1])
                if d < best[v]:
                    best[v] = d

    return total
