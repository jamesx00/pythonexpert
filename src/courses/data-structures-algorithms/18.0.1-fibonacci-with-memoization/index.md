---
lesson_name: "Warm-up: Fibonacci with Memoization"
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

### Warm-up: Fibonacci with Memoization

The Fibonacci numbers are `fib(0) = 0`, `fib(1) = 1`, and `fib(n) = fib(n - 1) + fib(n - 2)`.

The direct recursive version recomputes the same values again and again, taking roughly `2ⁿ` calls. `fib(40)` alone needs hundreds of millions of calls. Write a function `fib(n)` that is fast even for `n = 90` by **memoizing**: store each answer the first time you compute it and reuse it afterwards.

**Hint:** keep a dictionary `memo` inside `fib` and write an inner recursive function `f(i)`. At the start of `f`, `if i in memo: return memo[i]`. Before returning, save the result in `memo[i]`. (Python's `@functools.cache` decorator does the same thing for you; try writing it by hand first.)

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

With the memo, each `f(i)` is computed once, so the work drops from `O(2ⁿ)` to `O(n)`. This is **top-down DP**: write the plain recursion first, then add a cache. You'll use this exact move, recursion + memo, in many DP problems.

</details>
