---
lesson_name: Course Schedule
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(V + E)
  space: O(V + E)
hints:
  - "Draw each prerequisite as an edge between two courses. What shape in that graph makes it impossible to take every course?"
  - "Use the directed cycle check from *Tips & Gotchas* in *Graphs Basics*: run a DFS from every course with three states. A course is *visiting* while you explore its prerequisites and *done* afterwards. Reaching a *visiting* course again means there's a cycle."
  - "Template: `state = {}`. `dfs(node)`: if `state.get(node) == 0` (visiting), return `False`; if it's `1` (done), return `True`. Set `state[node] = 0`, return `False` if `dfs` fails for any prerequisite, then set `state[node] = 1` and return `True`. Return `True` only if `dfs` succeeds for every course."
rich_test_results: true
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 1
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 2
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Course Schedule

You must take `num_courses` courses, numbered `0` to `num_courses - 1`. You are given a list of prerequisite pairs `[course, prereq]`, meaning `course` cannot be taken until `prereq` is completed. Write a function `can_finish(num_courses, prerequisites)` that returns `True` if it is possible to take every course, and `False` if the prerequisites form a cycle that makes it impossible.

For example, with `num_courses = 2` and `prerequisites = [[1, 0]]`, course `1` requires course `0` first, which has no prerequisites of its own, so every course can be completed and the function should return `True`. If instead `prerequisites = [[1, 0], [0, 1]]`, the two courses each require the other, so nothing can ever be scheduled first, and the function should return `False`.

---

### Tests

<ul>
<li id="test-1"><code>can_finish(2, [[1, 0]])</code> should return <code>True</code></li>
<li id="test-2"><code>can_finish(2, [[1, 0], [0, 1]])</code> should return <code>False</code></li>
<li id="test-3"><code>can_finish(4, [[1, 0], [2, 1], [3, 2]])</code> should return <code>True</code></li>
<li id="test-4"><code>can_finish(3, [[0, 1], [1, 2], [2, 0]])</code> should return <code>False</code></li>
<li id="test-5"><code>can_finish(1, [])</code> should return <code>True</code></li>
<li id="test-6"><code>can_finish(5, [[1, 0], [2, 0], [3, 1], [3, 2]])</code> should return <code>True</code></li>
<li id="test-7"><code>can_finish(2, [])</code> should return <code>True</code></li>
<li id="test-8"><code>can_finish(1, [[0, 0]])</code> should return <code>False</code></li>
<li id="test-9"><code>can_finish(5, [[1, 0], [2, 1], [4, 3], [3, 4]])</code> should return <code>False</code></li>
<li id="test-10">Performance: 20,000 courses in 50 chains of 400, where each course needs the next two in its chain, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import defaultdict

def can_finish(num_courses, prerequisites):
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
```

Here `V` is `num_courses` and `E` is the number of prerequisite pairs.

**Brute force:** take courses in passes. On each pass over all the courses, take every course whose prerequisites are all taken, and stop when a pass takes nothing. A pass costs `O(V + E)` and there can be `V` passes: `O(V * (V + E))`. In test 10 each chain needs 400 passes over 20,000 courses. A DFS that only tracks the current path, without a *done* state, is even worse: it explores a shared prerequisite again for every path that reaches it, which grows exponentially.

**Bottleneck:** re-checking courses that haven't changed, or re-exploring courses already known to be fine.

**Optimal idea:** every course can be taken exactly when the prerequisite graph has no cycle. Look for cycles with one DFS that uses three states: unvisited, *visiting* (on the current DFS path) and *done*. Each course is explored once.

**Why it's correct:** if the DFS reaches a *visiting* course, the current path leads back to it, which is a cycle, so no order exists. A *done* course has already been fully explored without finding a cycle, so it's safe to skip. If no DFS finds a cycle, the courses can be taken in the order they became *done*, which always puts prerequisites first.

**Complexity:** `O(V + E)` time and space.

**Common mistakes:** using a plain `visited` set, which can't tell a cycle from a course reached twice along different paths (test 6 reaches course `0` through both `1` and `2`). Starting the DFS only from course `0`: a cycle can sit in a separate part of the graph (test 9). Kahn's algorithm from *Topological Sort* works too: the answer is `True` exactly when it places all `num_courses` courses.

</details>
