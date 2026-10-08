---
lesson_name: "Warm-up: Reverse a String"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n²)
hints:
  - "Which strings are their own reverse, so the function can return them straight away? If you could reverse everything except the first character, where would the first character go?"
  - "Use the *Shrink by one* shape in *Recursion Basics*: base case `len(s) <= 1` returns `s`, recursive case returns `reverse_string(s[1:]) + s[0]`."
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

### Warm-up: Reverse a String

Write a **recursive** function `reverse_string(s)` that returns `s` reversed. For example, `reverse_string("hello")` returns `"olleh"`.

Don't use slicing with a negative step (`s[::-1]`), `reversed()` or a loop: `reverse_string` must call itself.

---

### Tests

<ul>
<li id="test-1"><code>reverse_string(&#x27;&#x27;)</code> should return <code>&#x27;&#x27;</code></li>
<li id="test-2"><code>reverse_string(&#x27;a&#x27;)</code> should return <code>&#x27;a&#x27;</code></li>
<li id="test-3"><code>reverse_string(&#x27;ab&#x27;)</code> should return <code>&#x27;ba&#x27;</code></li>
<li id="test-4"><code>reverse_string(&#x27;hello&#x27;)</code> should return <code>&#x27;olleh&#x27;</code></li>
<li id="test-5"><code>reverse_string(&#x27;racecar&#x27;)</code> should return <code>&#x27;racecar&#x27;</code></li>
<li id="test-6"><code>reverse_string(&#x27;Python 3!&#x27;)</code> should return <code>&#x27;!3 nohtyP&#x27;</code></li>
<li id="test-7"><code>reverse_string(&#x27;abcdefghij&#x27; * 50)</code> should return <code>&#x27;jihgfedcba&#x27; * 50</code></li>
<li id="test-8"><code>reverse_string(&#x27;abc&#x27;)</code> calls itself</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
```

**Approach:** the empty string and one-character strings are their own reverse, so they're the base case. For anything longer, trust the recursion: `reverse_string(s[1:])` is the rest of the string reversed, and the first character belongs at the very end.

**Why it's correct:** each call works on a string one character shorter, so the length always reaches `1` or `0`. If the recursive call returns `s[1:]` reversed, then appending `s[0]` puts every character in reverse order. For `"abc"`: `reverse_string("bc") + "a"` = `(reverse_string("c") + "b") + "a"` = `"cba"`.

**Complexity:** `n` calls, but each one copies a slice (`s[1:]`) and builds a new string with `+`, both `O(n)`. That's `O(n²)` time, which is fine for the short strings recursion can handle anyway (Python's recursion limit is about 1,000).

**Going further (`O(n)`):** strings can't be changed in place, so every `+` copies. To get `O(n)`, recurse on an index and collect the characters in a list, then join it once:

```python
def reverse_string(s):
    chars = []

    def collect(i):
        if i < 0:
            return
        chars.append(s[i])
        collect(i - 1)

    collect(len(s) - 1)
    return "".join(chars)
```

**Common mistakes:** a base case of only `len(s) == 1`, so `reverse_string("")` recurses forever (until `RecursionError`). Returning `s[0] + reverse_string(s[1:])`, which rebuilds the original string. Forgetting `return` in front of the recursive call.

</details>
