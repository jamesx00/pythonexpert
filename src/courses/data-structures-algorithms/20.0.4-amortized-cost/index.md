---
lesson_name: "Warm-up: Amortized Cost"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
hints:
  - "An expensive step that happens rarely can still be cheap on average. Over `n` operations, how much work happens in total, and how many times can the expensive step happen?"
  - "Reread *Amortized Cost* in *Big-O Analysis Basics*. Add up the copies: with doubling they're `1 + 2 + 4 + … + n < 2n`, with growth by a fixed `10` they're `10 + 20 + 30 + … + n`. For `next_greater`, count how many times any one element can be pushed and popped."
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

### Warm-up: Amortized Cost

Amortized cost is the **average cost per operation over a whole sequence**, even if a single operation is sometimes expensive. `DoublingArray` and `GrowByTenArray` below are simplified dynamic arrays (like `list`, they copy everything into a bigger block when full). They differ only in how much they grow.

In this warm-up `n` is the number of appends (or `len(nums)`). Note which question each function asks: the total for the whole sequence, the cost of **one** call in the worst case, or the amortized cost of one call.

Each `..._complexity()` function in `main.py` returns `"O(?)"`. Replace it with the snippet's **time complexity** as a string (the worst case, unless the snippet's comment asks for something else), such as `"O(1)"`, `"O(n)"`, `"O(n^2)"` or `"O(n log n)"`. Spaces and capital letters don't matter, and `n²` and `n^2` are both fine. When there are two sizes, write both, e.g. `"O(n * m)"` or `"O(m log n)"`.

Work each answer out on paper first. You can run the snippets in `main.py` to experiment, but the goal is to read the complexity from the code.

#### `build_list`

```python
def build_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result
```

#### `append_one`

```python
class DoublingArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None]

    def append(self, value):
        if self.size == self.capacity:
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.size] = value
        self.size += 1


def append_one(array, value):
    # The worst-case cost of ONE call, on an array holding n items.
    array.append(value)
```

#### `append_amortized`

```python
def append_amortized(array, value):
    # The AMORTIZED cost of one call, over a long run of appends
    # to the same DoublingArray.
    array.append(value)
```

#### `fill_grow_by_ten`

```python
class GrowByTenArray:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.data = [None] * 10

    def append(self, value):
        if self.size == self.capacity:
            self.capacity += 10
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.size] = value
        self.size += 1


def fill_grow_by_ten(n):
    array = GrowByTenArray()
    for i in range(n):
        array.append(i)
    return array
```

#### `next_greater`

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # indexes still waiting for a bigger number
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

---

### Tests

<ul>
<li id="test-1"><code>build_list_complexity()</code> returns the time complexity of <code>build_list</code></li>
<li id="test-2"><code>append_one_complexity()</code> returns the time complexity of <code>append_one</code></li>
<li id="test-3"><code>append_amortized_complexity()</code> returns the time complexity of <code>append_amortized</code></li>
<li id="test-4"><code>fill_grow_by_ten_complexity()</code> returns the time complexity of <code>fill_grow_by_ten</code></li>
<li id="test-5"><code>next_greater_complexity()</code> returns the time complexity of <code>next_greater</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def build_list_complexity():
    return "O(n)"


def append_one_complexity():
    return "O(n)"


def append_amortized_complexity():
    return "O(1)"


def fill_grow_by_ten_complexity():
    return "O(n^2)"


def next_greater_complexity():
    return "O(n)"
```

**`build_list`: `O(n)`.** `n` appends at `O(1)` amortized each: `O(n)` in total. The occasional resize copies are already included in the amortized cost.

**`append_one`: `O(n)`.** If the array is full, this one call copies all `n` items into the new block. Most calls are `O(1)`, but the question asks for the worst case of a single call.

**`append_amortized`: `O(1)`.** Over `n` appends, resizes happen at sizes 1, 2, 4, 8, …, copying fewer than `2n` items in total. Add `n` writes and the whole sequence is `O(n)`, so each append is `O(1)` on average.

**`fill_grow_by_ten`: `O(n^2)`.** A resize happens every 10 appends and copies everything so far: `10 + 20 + 30 + … + n`, which is about `n²/20` copies, so `O(n²)` in total (`O(n)` amortized per append). This is why real dynamic arrays grow by **multiplying** the capacity.

**`next_greater`: `O(n)`.** The inner `while` can pop many items in one iteration, so it looks like `O(n²)`. But each index is pushed exactly once and popped at most once, so all the pops **across the whole run** add up to at most `n`. Total: `O(n)`. This argument (count the total work, not the worst single step) is amortized analysis again, and you'll use it in the *Stack* section.

**Common mistakes:** confusing the worst case of one operation (`append_one`, `O(n)`) with the amortized cost (`append_amortized`, `O(1)`). Assuming any resizing array has `O(1)` amortized append: that's only true when capacity grows by a constant **factor** (`fill_grow_by_ten` is `O(n²)`). Multiplying the worst case of an inner loop by the outer loop's length when the inner loop shares its work across the whole run (`next_greater`).

</details>
