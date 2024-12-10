---
lesson_name: Find Different Elements
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 401
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 400
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

### Finding different elements

Write a function that takes two lists as input and returns a new list containing the elements that are present in one list but not the other.

### Example

List 1: [1, 2, 3, 4, 5]<br />
List 2: [4, 5, 6, 7, 8]<br />
Expected Output: [1, 2, 3, 6, 7, 8]<br />
Explanation: Elements 1, 2, 3 are present in List 1 but not in List 2, while the elements 6, 7, 8 are present in List 2 but not in List 1.

### Tests

<ul>
<li id="test-1"><code>find_different_elements([1,2,3,4,5], [4,5,6,7,8])</code> should return <code>[1,2,3,6,7,8]</code></li>
<li id="test-2"><code>find_different_elements(['apple', 'banana', 'grape', 'orange'], ['banana', 'grape', 'kiwi', 'mango'])</code> should return <code>['apple', 'orange', 'kiwi', 'mango']</code></li>
<li id="test-3"><code>find_different_elements([1,2,3,4,5], [1,2,3,4,5])</code> should return <code>[]</code></li>
<li id="test-4"><code>find_different_elements([10, 20, 30, 40], [])</code> should return <code>[10, 20, 30, 40]</code></li>
<li id="test-5"><code>find_different_elements([], ['apple', 'banana', 'cherry'])</code> should return <code>['apple', 'banana', 'cherry']</code></li>
</ul>
