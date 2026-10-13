---
lesson_name: "Warm-up: Fibonacci with Memoization"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "Draw the calls for `fib(5)`. How many times is `fib(2)` computed? What if you wrote each answer down the first time?"
  - "Use *Top-down: recursion + memo* from *1-D Dynamic Programming Basics*: a dict `memo` inside `fib` and an inner `f(i)`. Return `memo[i]` if it's there; otherwise compute it, save it in `memo[i]`, and return it."
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

### Warm-up: Fibonacci with Memoization

The Fibonacci numbers are `fib(0) = 0`, `fib(1) = 1`, and `fib(n) = fib(n - 1) + fib(n - 2)`.

The direct recursive version recomputes the same values again and again, taking roughly `2ⁿ` calls. `fib(40)` alone needs hundreds of millions of calls. Write a function `fib(n)` that is fast even for `n = 90` by **memoizing**: store each answer the first time you compute it and reuse it afterwards.

---

### Tests

<ul>
<li id="test-1"><code>fib(0)</code> should return <code>0</code></li>
<li id="test-2"><code>fib(1)</code> should return <code>1</code></li>
<li id="test-3"><code>fib(2)</code> should return <code>1</code></li>
<li id="test-4"><code>fib(10)</code> should return <code>55</code></li>
<li id="test-5"><code>fib(30)</code> should return <code>832040</code></li>
<li id="test-6"><code>fib(90)</code> should return <code>2880067194370816120</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def fib(n):
    memo = {}

    def f(i):
        if i < 2:
            return i
        if i in memo:
            return memo[i]
        memo[i] = f(i - 1) + f(i - 2)
        return memo[i]

    return f(n)
```

**Brute force:** the plain recursion `fib(n - 1) + fib(n - 2)`. Each call makes two more, so it takes about `2^n` calls. `fib(30)` is already over a million calls, and `fib(90)` would never finish.

**Bottleneck:** the same values are computed again and again. `fib(n - 2)` is computed once by `fib(n)` and again inside `fib(n - 1)`, and the repeats multiply further down.

**Optimal idea:** there are only `n + 1` different questions, `fib(0)` to `fib(n)`. Save each answer in `memo` the first time it is computed, and look it up every time after that.

**Why it's correct:** memoizing doesn't change what is computed, only how often. `fib(i)` always has the same value, so a saved answer is as good as a fresh one.

**Complexity:** `O(n)` time: each `f(i)` does real work once, and every other call is a dict lookup. `O(n)` space for `memo` and the call stack.

**Common mistakes:** creating `memo` inside `f`, so every call starts with an empty dict and nothing is reused. Checking the memo but forgetting to store the result. A default argument `memo={}` works, but the dict is shared across calls of `fib`, which surprises people. Python's `@functools.cache` does all of this for you.

</details>
