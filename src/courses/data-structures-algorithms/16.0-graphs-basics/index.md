---
lesson_name: Graphs Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Graphs
---

## Why This Pattern Matters &#x1F4A1;

A graph is a set of **nodes** connected by **edges**. Social networks, course prerequisites, road maps, and even a 2-D grid of cells are all graphs. Almost every graph problem uses one of two traversals, **depth-first search (DFS)** or **breadth-first search (BFS)**, plus a `visited` set so you don't loop forever.

## Representing a Graph &#x1F5FA;&#xFE0F;

Problems usually hand you an **edge list**. Convert it to an **adjacency list** first:

```python
from collections import defaultdict

edges = [[0, 1], [0, 2], [1, 3]]
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)   # leave this out if edges are directed
```

**A grid is an implicit graph.** Each cell `(r, c)` is a node, and its neighbours are the up/down/left/right cells that are inside the grid:

```python
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for dr, dc in DIRECTIONS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        ...
```

## DFS: Go Deep First &#x1F573;&#xFE0F;

DFS follows one path as far as it can, then backs up and tries the next branch. Recursion handles the "backing up" for you.

```python
def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
```

The iterative version uses an explicit **stack**:

```python
def dfs_iterative(start, graph):
    visited, stack = {start}, [start]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return visited
```

**Use DFS for:** reachability, counting connected components / islands, cycle detection, topological sort, and exploring every path.

## BFS: Go Wide First &#x1F30A;

BFS visits every node 1 step away, then every node 2 steps away, and so on, using a **queue**. Because it explores in rings of increasing distance, **the first time BFS reaches a node is along a shortest path** (when every edge has the same cost).

```python
from collections import deque

def bfs_distances(start, graph):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:          # dist doubles as visited
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist
```

**Use BFS for:** shortest path in an unweighted graph, "minimum number of steps/moves", spreading processes (*Rotting Oranges*), and level-by-level work.

**Multi-source BFS:** if many starting points spread at the same time, put **all** of them in the queue at the start, each with distance `0`.

## DFS or BFS? &#x2696;&#xFE0F;

| Question | Use |
| --- | --- |
| Can I reach X? How many components? | Either (DFS is shorter to write) |
| Fewest steps / shortest unweighted path | **BFS** |
| Detect a cycle, topological order | **DFS** (or Kahn's BFS for topo) |
| Connectivity as edges are added | **Union-find** |
| Weighted shortest path | **Dijkstra** (Advanced Graphs) |

## Topological Sort &#x1F4CB;

For a **directed acyclic graph** (like course prerequisites), a topological order lists every node after all the nodes it depends on. Kahn's algorithm is a BFS over nodes with no remaining prerequisites:

```python
from collections import deque

def topo_sort(n, edges):          # edge [a, b] means a -> b
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1
    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order if len(order) == n else []   # shorter = there was a cycle
```

## Union-Find &#x1F517;

When edges arrive one at a time and you only care **which nodes are connected** (not the paths between them), union-find is simpler than repeated DFS. Each node points to a parent, and following parents leads to a group's root:

```python
parent = list(range(n))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path compression
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False        # already connected → this edge closes a cycle
    parent[ra] = rb
    return True
```

**Use it for:** counting components as edges are added, detecting a redundant edge in an undirected graph, and checking whether a graph is a valid tree (`n - 1` edges, no `union` returns `False`).

## Tips & Gotchas &#x1F4CC;

- **Mark visited when you enqueue/push, not when you pop.** Otherwise the same node can enter the queue many times.
- **Loop over every node** to start traversals (`for node in range(n): if node not in visited: ...`). The graph may be disconnected. Count how many times you start a traversal to get the number of components.
- **Grids: you can mark visited in place** (e.g. turn `"1"` into `"0"`) instead of keeping a set, if you're allowed to modify the input.
- **Cycle detection in a directed graph** needs three states: unvisited, *visiting* (on the current path), and *done*. Reaching a *visiting* node means there's a cycle.
- **Undirected cycle check:** in DFS, skip the parent you just came from, or use union-find.
- **Don't `list.pop(0)` for a queue.** It's `O(n)`. Use `collections.deque`.
- **Python recursion limit (~1000)** can break DFS on big grids. Use an iterative stack or `sys.setrecursionlimit`.
- Complexity for both traversals: `O(V + E)` time, `O(V)` space. For a grid that's `O(rows × cols)`.

The warm-up exercises that follow have you build each of these from scratch before the interview problems.
