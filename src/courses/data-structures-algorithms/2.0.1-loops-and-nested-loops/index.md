---
lesson_name: "Warm-up: Loops and Nested Loops"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
hints:
  - "For each loop, ask: how many times does its body run, as a function of the input size? Does that number change when the input doubles?"
  - "Use the rules in *Big-O Analysis Basics*: loops one after another **add** (keep the biggest), loops inside each other **multiply**. A loop that runs a fixed number of times, whatever the input, is `O(1)`."
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

### Warm-up: Loops and Nested Loops

Each snippet below takes a list (or two). Work out how many times the innermost line runs in the worst case, then drop constants and lower-order terms. In this warm-up `n` is `len(nums)`. In `count_common`, `n` is `len(a)` and `m` is `len(b)`.

Each `..._complexity()` function in `main.py` returns `"O(?)"`. Replace it with the snippet's **time complexity** as a string (the worst case, unless the snippet's comment asks for something else), such as `"O(1)"`, `"O(n)"`, `"O(n^2)"` or `"O(n log n)"`. Spaces and capital letters don't matter, and `n²` and `n^2` are both fine. When there are two sizes, write both, e.g. `"O(n * m)"` or `"O(m log n)"`.

Work each answer out on paper first. You can run the snippets in `main.py` to experiment, but the goal is to read the complexity from the code.

#### `total`

```python
def total(nums):
    result = 0
    for x in nums:
        result += x
    return result
```

#### `has_duplicate`

```python
def has_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

#### `min_and_max`

```python
def min_and_max(nums):
    smallest = nums[0]
    for x in nums:
        smallest = min(smallest, x)
    largest = nums[0]
    for x in nums:
        largest = max(largest, x)
    return smallest, largest
```

#### `count_common`

```python
def count_common(a, b):
    count = 0
    for x in a:
        for y in b:
            if x == y:
                count += 1
    return count
```

#### `first_ten_sum`

```python
def first_ten_sum(nums):
    result = 0
    for i in range(min(10, len(nums))):
        result += nums[i]
    return result
```

#### `count_zero_triples`

```python
def count_zero_triples(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    count += 1
    return count
```

---

### Tests

<ul>
<li id="test-1"><code>total_complexity()</code> returns the time complexity of <code>total</code></li>
<li id="test-2"><code>has_duplicate_complexity()</code> returns the time complexity of <code>has_duplicate</code></li>
<li id="test-3"><code>min_and_max_complexity()</code> returns the time complexity of <code>min_and_max</code></li>
<li id="test-4"><code>count_common_complexity()</code> returns the time complexity of <code>count_common</code></li>
<li id="test-5"><code>first_ten_sum_complexity()</code> returns the time complexity of <code>first_ten_sum</code></li>
<li id="test-6"><code>count_zero_triples_complexity()</code> returns the time complexity of <code>count_zero_triples</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def total_complexity():
    return "O(n)"


def has_duplicate_complexity():
    return "O(n^2)"


def min_and_max_complexity():
    return "O(n)"


def count_common_complexity():
    return "O(n * m)"


def first_ten_sum_complexity():
    return "O(1)"


def count_zero_triples_complexity():
    return "O(n^3)"
```

**`total`: `O(n)`.** The loop body runs once per element, and each step is `O(1)`. `n` steps → `O(n)`.

**`has_duplicate`: `O(n^2)`.** In the worst case (no duplicates) the inner loop runs `n - 1`, then `n - 2`, …, then `0` times. That adds up to `n(n - 1)/2`, which is `O(n²)`. Starting `j` at `i + 1` halves the work, but halving is a constant factor.

**`min_and_max`: `O(n)`.** Two loops one **after** the other: `n + n = 2n` steps, which is `O(n)`. Sequential loops add, they don't multiply.

**`count_common`: `O(n * m)`.** The inner loop runs `m` times for each of the `n` outer iterations: `n · m` steps. Writing `O(n²)` is only right when both lists have the same length.

**`first_ten_sum`: `O(1)`.** The loop runs at most 10 times, however long `nums` is. A loop doesn't make code `O(n)`. What matters is whether its number of iterations grows with the input.

**`count_zero_triples`: `O(n^3)`.** Three nested loops, each running up to `n` times. The exact count is `n(n - 1)(n - 2)/6` triples, which is `O(n³)`.

**How to approach any snippet:** find the line that runs most often, count how many times it runs as a function of the input size, then drop constant factors and smaller terms.

**Common mistakes:** multiplying sequential loops (`min_and_max` is not `O(n²)`). Calling any loop `O(n)` without checking what it loops over (`first_ten_sum`). Collapsing two different sizes into one `n` (`count_common` is `O(n · m)`). Keeping constants such as `O(n²/2)` or `O(2n)`.

</details>
