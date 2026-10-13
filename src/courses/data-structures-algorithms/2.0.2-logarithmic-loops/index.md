---
lesson_name: "Warm-up: Logarithmic Loops"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
hints:
  - "If a variable is multiplied or divided by a constant each step, how many steps does it take to get from `1` to `n` (or from `n` down to `1`)?"
  - "Repeated halving or doubling takes about `log n` steps (*Big-O Analysis Basics*, *Halving the input each step gives a log*). Then multiply by whatever surrounds the loop. In `halving_work`, add up the inner loop's iterations across all rounds instead of multiplying."
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

### Warm-up: Logarithmic Loops

Every snippet here contains a loop whose variable is multiplied or divided instead of increased by one. In this warm-up `n` is the number passed in, or `len(nums)`. In `search_all`, `n` is `len(nums)` and `m` is `len(queries)`.

Each `..._complexity()` function in `main.py` returns `"O(?)"`. Replace it with the snippet's **time complexity** as a string (the worst case, unless the snippet's comment asks for something else), such as `"O(1)"`, `"O(n)"`, `"O(n^2)"` or `"O(n log n)"`. Spaces and capital letters don't matter, and `n²` and `n^2` are both fine. When there are two sizes, write both, e.g. `"O(n * m)"` or `"O(m log n)"`.

Work each answer out on paper first. You can run the snippets in `main.py` to experiment, but the goal is to read the complexity from the code.

#### `count_digits`

```python
def count_digits(n):
    digits = 1
    while n >= 10:
        n //= 10
        digits += 1
    return digits
```

#### `largest_power_of_two`

```python
def largest_power_of_two(n):
    power = 1
    while power * 2 <= n:
        power *= 2
    return power
```

#### `halvings_per_index`

```python
def halvings_per_index(n):
    total = 0
    for i in range(n):
        j = n
        while j > 1:
            j //= 2
            total += 1
    return total
```

#### `count_distinct`

```python
def count_distinct(nums):
    nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            count += 1
    return count
```

#### `search_all`

```python
def search_all(nums, queries):
    # nums is sorted
    found = 0
    for q in queries:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == q:
                found += 1
                break
            if nums[mid] < q:
                lo = mid + 1
            else:
                hi = mid - 1
    return found
```

#### `halving_work`

```python
def halving_work(n):
    steps = 0
    size = n
    while size > 0:
        for _ in range(size):
            steps += 1
        size //= 2
    return steps
```

---

### Tests

<ul>
<li id="test-1"><code>count_digits_complexity()</code> returns the time complexity of <code>count_digits</code></li>
<li id="test-2"><code>largest_power_of_two_complexity()</code> returns the time complexity of <code>largest_power_of_two</code></li>
<li id="test-3"><code>halvings_per_index_complexity()</code> returns the time complexity of <code>halvings_per_index</code></li>
<li id="test-4"><code>count_distinct_complexity()</code> returns the time complexity of <code>count_distinct</code></li>
<li id="test-5"><code>search_all_complexity()</code> returns the time complexity of <code>search_all</code></li>
<li id="test-6"><code>halving_work_complexity()</code> returns the time complexity of <code>halving_work</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def count_digits_complexity():
    return "O(log n)"


def largest_power_of_two_complexity():
    return "O(log n)"


def halvings_per_index_complexity():
    return "O(n log n)"


def count_distinct_complexity():
    return "O(n log n)"


def search_all_complexity():
    return "O(m log n)"


def halving_work_complexity():
    return "O(n)"
```

**`count_digits`: `O(log n)`.** Each step divides `n` by 10, so the loop runs once per digit: about `log₁₀ n` times. The base of a logarithm is a constant factor (`log₁₀ n = log₂ n / log₂ 10`), so it's just `O(log n)`.

**`largest_power_of_two`: `O(log n)`.** `power` doubles each step: 1, 2, 4, …, so it reaches `n` after about `log₂ n` steps.

**`halvings_per_index`: `O(n log n)`.** The outer loop runs `n` times. Each time, the inner loop halves `j` from `n` down to `1`, which is about `log n` steps. Nested loops multiply: `n · log n`.

**`count_distinct`: `O(n log n)`.** Sorting is `O(n log n)`, and the loop after it is `O(n)`. The two run one after the other, so they add, and the bigger term wins: `O(n log n)`.

**`search_all`: `O(m log n)`.** Each of the `m` queries runs a binary search over `nums`, which halves the range each step: `O(log n)` per query, `O(m log n)` in total.

**`halving_work`: `O(n)`.** It looks like `O(n log n)` (an `O(n)` loop inside an `O(log n)` loop), but the inner loop shrinks each round. Its total is `n + n/2 + n/4 + … < 2n`, so the whole function is `O(n)`. When the inner loop's length changes from round to round, add up the actual iterations instead of multiplying the worst cases.

**Common mistakes:** writing `O(n)` for a loop just because it's a `while` loop, without checking how fast the variable changes. Forgetting the cost of `sorted()` (`count_distinct`). Multiplying worst cases when the inner loop shrinks (`halving_work` is `O(n)`, not `O(n log n)`).

</details>
