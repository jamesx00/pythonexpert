---
lesson_name: Better String Replace
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 403
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 402
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

### Better string replace

Write a function that replaces a text in a string with another text while keeping the case of the first character of the word being replaced.

For example, to replace the text `"Python"` with `"apple"`, the text should become `"Apple"`.

---

### Tests

<ul>
<li id="test-1"><code>replace_text("Python is a popular programming language.", "Python", "javaScript")</code> should return <code>"JavaScript is a popular programming language."</code></li>
<li id="test-2"><code>replace_text("The Quick Brown Fox Jumps Over The Lazy Dog.", "Quick", "fast")</code> should return <code>"The Fast Brown Fox Jumps Over The Lazy Dog."</code></li>
<li id="test-3"><code>replace_text("The quick brown fox jumps over the lazy dog.", "quick", "Fast")</code> should return <code>"The fast brown fox jumps over the lazy dog."</code></li>
<li id="test-4"><code>replace_text("I have a cat and a dog. My cat's name is Whiskers.", "Whiskers", "coco")</code> should return <code>"I have a cat and a dog. My cat's name is Coco."</code></li>
</ul>
