---
lesson_name: Is This Pangram
code_editor: True
code_execution: True
adding_file_allowed: False
section: Intermediate Algorithm
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 393
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 392
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

### Is this pangram

Write a function that takes a sentence as input and determines whether it is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once, regardless of case.

#### Tips

Make sure to handle both uppercase and lowercase letters when checking for pangram condition.

---

### Tests

<ul>
<li id="test-1"><code>is_this_pangram("The quick brown fox jumps over the lazy dog.")</code> should return <code>True</code></li>
<li id="test-2"><code>is_this_pangram("Pack my box with five dozen liquor jugs.")</code> should return <code>True</code></li>
<li id="test-3"><code>is_this_pangram("Python is an amazing programming language.")</code> should return <code>False</code></li>
<li id="test-4"><code>is_this_pangram("Mr. Jock, TV quiz PhD, bags few lynx.")</code> should return <code>True</code></li>
<li id="test-5"><code>is_this_pangram("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")</code> should return <code>False</code></li>
</ul>
