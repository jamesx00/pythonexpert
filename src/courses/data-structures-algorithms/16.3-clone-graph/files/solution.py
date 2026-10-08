def clone_graph(adj_list):
    if not adj_list:
        return []

    clones = {}

    def dfs(node):
        if node in clones:
            return clones[node]
        clones[node] = []
        for neighbor in adj_list[node]:
            clones[node].append(neighbor)
        for neighbor in adj_list[node]:
            dfs(neighbor)
        return clones[node]

    dfs(0)
    return [clones[i] for i in range(len(adj_list))]
