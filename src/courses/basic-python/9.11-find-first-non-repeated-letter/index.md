---
lesson_name: Find First Non-Repeated Letter
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 408
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 409
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

### Find first non-repeated character

Write a function that takes a string as input and returns the first non-repeated character in the string while ignoring the case. If there are no non-repeated characters, the function should return `None`.

Repeated characters is a character that is repeated directly next to each other. For example, `"aa"`, `"Aa"`, and `"aAa"`, are all repeated characters, but `"aba"` is not.

---

### Tests

<ul>
<li id="test-1"><code>find_first_non_repeated_character("aabbccdd")</code> should return <code>None</code></li>
<li id="test-2"><code>find_first_non_repeated_character("aabbccd")</code> should return <code>"d"</code></li>
<li id="test-3"><code>find_first_non_repeated_character("abcd")</code> should return <code>"a"</code></li>
<li id="test-4"><code>find_first_non_repeated_character("001112222233454")</code> should return <code>"4"</code></li>
<li id="test-5"><code>find_first_non_repeated_character("aaABbbcC00==5665OO")</code> should return <code>"5"</code></li>
</ul>
