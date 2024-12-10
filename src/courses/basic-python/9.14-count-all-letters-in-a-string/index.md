---
lesson_name: Count All Letters in a String
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 434
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 433
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

### Count all letters in a string

Write a function that takes a string as input and count the occurrence of each letter (case-insensitive) and return a dictionary with the characters as keys and their respective counts as values. Only count English alphabet and ignore everything else.

---

### Tests

<ul>
<li id="test-1"><code>count_letters("Hello World!")</code> should return <code>{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}</code></li>
<li id="test-2"><code>count_letters("Python is Fun!")</code> should return <code>{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 2, 'i': 1, 's': 1, 'f': 1, 'u': 1}</code></li>
<li id="test-3"><code>count_letters("Mississippi")</code> should return <code>{'m': 1, 'i': 4, 's': 4, 'p': 2}</code></li>
<li id="test-4"><code>count_letters("OpenAI+")</code> should return <code>{'o': 1, 'p': 1, 'e': 1, 'n': 1, 'a': 1, 'i': 1}</code></li>
<li id="test-5"><code>count_letters("Abra Kadabra")</code> should return <code>{'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1}</code></li>
</ul>
