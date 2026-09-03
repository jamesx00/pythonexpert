---
lesson_name: Set Matrix Zeroes
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

### Set Matrix Zeroes

You're given a grid of integers, `matrix`. Write a function that finds every cell containing `0`, and for each one zeroes out its entire row and entire column. The change must be made in place on `matrix`, and your function should return that same mutated `matrix`.

For example, given
```
[[1, 2, 3],
 [4, 0, 6],
 [7, 8, 9]]
```
the `0` sits at row 1, column 1, so row 1 and column 1 both get zeroed out, producing
```
[[1, 0, 3],
 [0, 0, 0],
 [7, 0, 9]]
```

---

### Tests

<ul>
<li id="test-1"><code>set_zeroes([[1, 2, 3], [4, 0, 6], [7, 8, 9]])</code> should return <code>[[1, 0, 3], [0, 0, 0], [7, 0, 9]]</code></li>
<li id="test-2"><code>set_zeroes([[0, 1], [1, 1]])</code> should return <code>[[0, 0], [0, 1]]</code></li>
<li id="test-3"><code>set_zeroes([[1, 2], [3, 4]])</code> should return <code>[[1, 2], [3, 4]]</code></li>
<li id="test-4"><code>set_zeroes([[1, 0, 3], [4, 5, 6], [0, 8, 9]])</code> should return <code>[[0, 0, 0], [0, 0, 6], [0, 0, 0]]</code></li>
<li id="test-5"><code>set_zeroes([[5]])</code> should return <code>[[5]]</code></li>
<li id="test-6"><code>set_zeroes([[0]])</code> should return <code>[[0]]</code></li>
</ul>
