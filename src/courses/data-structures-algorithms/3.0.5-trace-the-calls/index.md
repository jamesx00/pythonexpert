---
lesson_name: "Warm-up: Trace the Calls"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
hints:
  - "Draw the call tree for `fib(4)` on paper: `fib(4)` at the top, with `fib(3)` and `fib(2)` underneath. Keep expanding until every leaf is `fib(1)` or `fib(0)`. Which branch runs first?"
  - "Calls start in the order a depth-first walk reaches them: go all the way down the left branch (`fib(n - 1)`) before starting the right branch (`fib(n - 2)`). A call **returns** only after both of its children have returned. For `count_x_buggy`, look at what happens to the value of `1 + count_x_buggy(s[1:])`."
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

### Warm-up: Trace the Calls

Tracing a recursive function by hand is the most reliable way to understand it, and to debug it. This exercise walks you through it in steps. Answer each one on paper first, then put your answer in `main.py`. (You can check your answers afterwards by adding `print` calls to `fib`, but working them out yourself is the point.)

`main.py` contains these two functions:

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def count_x_buggy(s):
    """Meant to count how many times "x" appears in s. It has a bug."""
    if s == "":
        return 0
    if s[0] == "x":
        1 + count_x_buggy(s[1:])
    return count_x_buggy(s[1:])
```

**Step 1: the order calls start.** Calling `fib(4)` sets off a whole tree of calls. Make `fib_call_order()` return a list of the `n` passed to each call to `fib`, **in the order the calls start**, beginning with `4`.

**Step 2: the order calls return.** Make `fib_return_order()` return a list of the **values returned** by those calls, in the order they return. The last one is `fib(4)`'s own result.

**Step 3: the deepest point.** Make `fib_max_depth()` return the largest number of `fib` calls that are running at the same time (waiting on the call stack, including the one currently running) during `fib(4)`.

**Step 4: the total.** Make `fib_total_calls()` return how many times `fib` is called in total during `fib(4)`, including the first call.

**Step 5: find the bug.** Trace `count_x_buggy("xax")` and make `buggy_result()` return what it actually returns.

**Step 6: fix it.** Write `count_x(s)`, a fixed **recursive** version that returns how many times `"x"` appears in `s`.

---

### Tests

<ul>
<li id="test-1"><code>fib_call_order()</code> returns the arguments of the calls made by <code>fib(4)</code>, in the order they start</li>
<li id="test-2"><code>fib_return_order()</code> returns the values returned by those calls, in the order they return</li>
<li id="test-3"><code>fib_max_depth()</code> returns the maximum call-stack depth reached by <code>fib(4)</code></li>
<li id="test-4"><code>fib_total_calls()</code> returns the total number of calls made by <code>fib(4)</code></li>
<li id="test-5"><code>buggy_result()</code> returns what <code>count_x_buggy(&#x27;xax&#x27;)</code> actually returns</li>
<li id="test-6"><code>count_x(&#x27;&#x27;)</code> should return <code>0</code></li>
<li id="test-7"><code>count_x(&#x27;abc&#x27;)</code> should return <code>0</code></li>
<li id="test-8"><code>count_x(&#x27;xax&#x27;)</code> should return <code>2</code></li>
<li id="test-9"><code>count_x(&#x27;xxxx&#x27;)</code> should return <code>4</code></li>
<li id="test-10"><code>count_x(&#x27;axbxcx&#x27;)</code> should return <code>3</code></li>
<li id="test-11"><code>count_x(&#x27;xax&#x27;)</code> calls itself</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def fib_call_order():
    return [4, 3, 2, 1, 0, 1, 2, 1, 0]


def fib_return_order():
    return [1, 0, 1, 1, 2, 1, 0, 1, 3]


def fib_max_depth():
    return 4


def fib_total_calls():
    return 9


def buggy_result():
    return 0


def count_x(s):
    if s == "":
        return 0
    if s[0] == "x":
        return 1 + count_x(s[1:])
    return count_x(s[1:])
```

**The call tree for `fib(4)`.** Each call to `fib(n)` with `n >= 2` calls `fib(n - 1)` first and, only after that has completely finished, `fib(n - 2)`:

```
fib(4)                                   returns 3
├─ fib(3)                                returns 2
│  ├─ fib(2)                             returns 1
│  │  ├─ fib(1)                          returns 1
│  │  └─ fib(0)                          returns 0
│  └─ fib(1)                             returns 1
└─ fib(2)                                returns 1
   ├─ fib(1)                             returns 1
   └─ fib(0)                             returns 0
```

**Step 1:** reading the tree top to bottom gives the order calls start: `4, 3, 2, 1, 0, 1, 2, 1, 0`. This is a depth-first, left-first walk.

**Step 2:** a call returns only after all of its children have returned, so leaves return first: `fib(1)` → `1`, `fib(0)` → `0`, then their parent `fib(2)` → `1`, then `fib(1)` → `1`, then `fib(3)` → `2`, and so on, ending with `fib(4)` → `3`. Filling in return values bottom-up like this is exactly how you check a recursive function by hand.

**Step 3:** the longest chain from the root to a leaf is `fib(4)` → `fib(3)` → `fib(2)` → `fib(1)`: 4 frames on the stack at once. The stack depth, not the total number of calls, is what determines the space a recursive function uses.

**Step 4:** count the nodes in the tree: 9. The tree roughly doubles with each extra level, which is why plain recursive `fib` is exponential.

**Step 5:** in `count_x_buggy("xax")`, the first character is `"x"`, so it computes `1 + count_x_buggy("ax")`, then **throws the result away** because that line doesn't return it. It then returns `count_x_buggy("ax")`, which returns `count_x_buggy("x")`, which (throwing away another result) returns `count_x_buggy("")` = `0`. Every path ends in the base case's `0` and nothing is ever added, so the answer is `0`.

**Step 6:** add the missing `return`, so the `+ 1` actually reaches the caller.

**Complexity of `count_x`:** `n + 1` calls, each copying a slice, so `O(n²)` time and `O(n)` stack depth. Passing an index instead of slicing makes it `O(n)`.

**Common mistakes:** listing calls breadth-first (`4, 3, 2, …`, level by level) instead of depth-first. Python finishes the whole `fib(n - 1)` subtree before starting `fib(n - 2)`. Counting depth from `0`. Reading the buggy function as if the unused expression had been returned.

</details>
