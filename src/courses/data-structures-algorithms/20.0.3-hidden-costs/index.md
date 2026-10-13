---
lesson_name: "Warm-up: Hidden Costs"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
hints:
  - "Look at each line inside the loop. Is it really one step, or is it a loop in disguise? What does Python have to do to answer `x in seen` when `seen` is a list?"
  - "Use the *Hidden loops count too* table in *Big-O Analysis Basics*. Multiply the cost of the expensive line by the number of times the loop runs it. A `collections.deque` removes from the left in `O(1)`."
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

### Warm-up: Hidden Costs

Each snippet has a single loop, but some of the lines inside cost more than one step. In this warm-up `n` is `len(nums)`.

Each `..._complexity()` function in `main.py` returns `"O(?)"`. Replace it with the snippet's **time complexity** as a string (the worst case, unless the snippet's comment asks for something else), such as `"O(1)"`, `"O(n)"`, `"O(n^2)"` or `"O(n log n)"`. Spaces and capital letters don't matter, and `n²` and `n^2` are both fine. When there are two sizes, write both, e.g. `"O(n * m)"` or `"O(m log n)"`.

Work each answer out on paper first. You can run the snippets in `main.py` to experiment, but the goal is to read the complexity from the code.

#### `has_duplicate_list`

```python
def has_duplicate_list(nums):
    seen = []
    for x in nums:
        if x in seen:
            return True
        seen.append(x)
    return False
```

#### `has_duplicate_set`

```python
def has_duplicate_set(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

#### `reversed_copy`

```python
def reversed_copy(nums):
    result = []
    for x in nums:
        result.insert(0, x)
    return result
```

#### `drain_list`

```python
def drain_list(nums):
    queue = list(nums)
    total = 0
    while queue:
        total += queue.pop(0)
    return total
```

#### `drain_deque`

```python
from collections import deque


def drain_deque(nums):
    queue = deque(nums)
    total = 0
    while queue:
        total += queue.popleft()
    return total
```

#### `prefix_sums`

```python
def prefix_sums(nums):
    result = []
    for i in range(len(nums)):
        result.append(sum(nums[:i + 1]))
    return result
```

---

### Tests

<ul>
<li id="test-1"><code>has_duplicate_list_complexity()</code> returns the time complexity of <code>has_duplicate_list</code></li>
<li id="test-2"><code>has_duplicate_set_complexity()</code> returns the time complexity of <code>has_duplicate_set</code></li>
<li id="test-3"><code>reversed_copy_complexity()</code> returns the time complexity of <code>reversed_copy</code></li>
<li id="test-4"><code>drain_list_complexity()</code> returns the time complexity of <code>drain_list</code></li>
<li id="test-5"><code>drain_deque_complexity()</code> returns the time complexity of <code>drain_deque</code></li>
<li id="test-6"><code>prefix_sums_complexity()</code> returns the time complexity of <code>prefix_sums</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def has_duplicate_list_complexity():
    return "O(n^2)"


def has_duplicate_set_complexity():
    return "O(n)"


def reversed_copy_complexity():
    return "O(n^2)"


def drain_list_complexity():
    return "O(n^2)"


def drain_deque_complexity():
    return "O(n)"


def prefix_sums_complexity():
    return "O(n^2)"
```

**`has_duplicate_list`: `O(n^2)`.** `x in seen` scans the list, and `seen` grows to `n` items, so the loop does `0 + 1 + … + (n - 1)` comparisons: `O(n²)`.

**`has_duplicate_set`: `O(n)`.** Same loop, but a set lookup and insert are `O(1)` on average, so it's `n` cheap steps: `O(n)`. Changing one data structure turns `O(n²)` into `O(n)`.

**`reversed_copy`: `O(n^2)`.** Inserting at the front shifts every item already in `result` one slot to the right. That's `0 + 1 + … + (n - 1)` moves: `O(n²)`. Appending and reversing at the end (or `nums[::-1]`) is `O(n)`.

**`drain_list`: `O(n^2)`.** `pop(0)` removes the first item and shifts all the others left, which is `O(n)`. Doing it `n` times is `O(n²)`.

**`drain_deque`: `O(n)`.** A `deque` is built for removing from both ends: `popleft()` is `O(1)`, so `n` of them is `O(n)`. Building the deque is also `O(n)`.

**`prefix_sums`: `O(n^2)`.** At step `i`, the slice `nums[:i + 1]` copies `i + 1` items and `sum` adds them up, so the total is `1 + 2 + … + n`: `O(n²)`. Keeping a running total gives `O(n)`.

**Common mistakes:** counting `x in some_list`, `insert(0, x)`, `pop(0)`, slicing or `sum()` as one step. Each of these is `O(n)` and, inside a loop, makes the whole function `O(n²)`. Assuming `in` costs the same on a list and a set.

</details>
