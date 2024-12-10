---
lesson_name: Chunking a List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 309
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 308
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
    id: 1
    name: Python
---

### Chunking a list

Write a function that takes a list and a specific chunk length as input and returns a new list with sublists, where each sublist has the specified chunk length.

---

### Tests

<ul>
<li id="test-1"><code>chunk_it_up([1, 2, 3, 4, 5, 6, 7, 8], 2)</code> should return <code>[[1, 2], [3, 4], [5, 6], [7, 8]]</code>.
<li id="test-2"><code>chunk_it_up(['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango'], 4)</code> should return <code>[['apple', 'banana', 'orange', 'grape'], ['kiwi', 'mango']]</code>.
<li id="test-3"><code>chunk_it_up([True, False, True, True], 1)</code> should return <code>[[True], [False], [True], [True]]</code>.
<li id="test-4"><code>chunk_it_up([10, 20, 30, 40, 50], 6)</code> should return <code>[[10, 20, 30, 40, 50]]</code>.
<li id="test-5"><code>chunk_it_up([], 3)</code> should return <code>[]</code>.
</ul>
