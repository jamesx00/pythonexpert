def clone_graph(adj_list):
    clones = {}

    def dfs(node):
        if node in clones:
            return
        clones[node] = []
        for neighbor in adj_list[node]:
            clones[node].append(neighbor)
            dfs(neighbor)

    for node in range(len(adj_list)):
        dfs(node)
    return [clones[node] for node in range(len(adj_list))]
