---
lesson_name: Course Schedule II
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(V + E)
  space: O(V + E)
hints:
  - "*Course Schedule* told you whether an order exists. When a DFS finishes a course, what do you know about all of that course's prerequisites?"
  - "Use *Topological Sort* from *Graphs Basics*: the three-state DFS from *Course Schedule*, plus a list. Append a course when it becomes *done*: all of its prerequisites were appended before it. If a DFS finds a cycle, return `[]`. (Kahn's algorithm gives an order directly, too.)"
  - "Template: `dfs(node)` as in *Course Schedule*, with `order.append(node)` right after `state[node] = 1`. Call it on every course, return `[]` as soon as one call finds a cycle, and return `order` at the end."
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

### Course Schedule II

You must take `num_courses` courses, numbered `0` to `num_courses - 1`. You are given a list of prerequisite pairs `[course, prereq]`, meaning `course` cannot be taken until `prereq` is completed. Write a function `find_order(num_courses, prerequisites)` that returns an order in which all courses can be taken satisfying every prerequisite, or an empty list if no valid order exists because the prerequisites form a cycle. If more than one valid order exists, any one of them is acceptable.

For example, with `num_courses = 3` and `prerequisites = [[1, 0], [2, 1]]`, course `1` needs course `0` first and course `2` needs course `1` first, so the only valid order is `[0, 1, 2]`.

---

### Tests

<ul>
<li id="test-1"><code>find_order(3, [[1, 0], [2, 1]])</code> should return a valid order such as <code>[0, 1, 2]</code></li>
<li id="test-2"><code>find_order(2, [[1, 0]])</code> should return a valid order such as <code>[0, 1]</code></li>
<li id="test-3"><code>find_order(2, [[1, 0], [0, 1]])</code> should return <code>[]</code></li>
<li id="test-4"><code>find_order(1, [])</code> should return a valid order such as <code>[0]</code></li>
<li id="test-5"><code>find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])</code> should return a valid order such as <code>[0, 1, 2, 3]</code></li>
<li id="test-6"><code>find_order(3, [])</code> should return a valid order such as <code>[0, 1, 2]</code> (any order)</li>
<li id="test-7"><code>find_order(4, [[0, 3], [3, 1], [1, 2]])</code> should return <code>[2, 1, 3, 0]</code></li>
<li id="test-8"><code>find_order(5, [[1, 0], [2, 1], [4, 3], [3, 4]])</code> should return <code>[]</code></li>
<li id="test-9">Performance: 20,000 courses in 50 chains of 400, where each course needs the next two in its chain, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
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
```

Here `V` is `num_courses` and `E` is the number of prerequisite pairs.

**Brute force:** take courses in passes. Each pass over all the courses takes every course whose prerequisites are all taken. When the prerequisite chains are long, that's `O(V * (V + E))`: test 9 needs 400 passes over 20,000 courses.

**Bottleneck:** each pass re-checks courses whose prerequisites haven't changed.

**Optimal idea:** in a DFS that follows course -> prerequisite edges, a course finishes only after all of its prerequisites have finished. So the finishing order (post-order) is a valid order. The three states catch cycles, as in *Course Schedule*.

**Why it's correct:** when a course is appended, every prerequisite has already been fully explored and appended, by this DFS or an earlier one. So each prerequisite comes before its course in `order`. The outer loop starts a DFS from every course, so each course is appended exactly once. A cycle makes `dfs` return `False`, and the answer is `[]`.

**Complexity:** `O(V + E)` time and space.

**Common mistakes:** building the edges as prerequisite -> course and then forgetting to reverse the post-order, which puts every course before its prerequisites. Returning the partial order when there's a cycle (test 8). Kahn's algorithm from *Topological Sort* gives a valid order directly, with no reversing.

</details>
