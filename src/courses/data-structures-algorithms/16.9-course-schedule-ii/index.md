---
lesson_name: Course Schedule II
code_editor: True
code_execution: True
adding_file_allowed: False
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

</details>
