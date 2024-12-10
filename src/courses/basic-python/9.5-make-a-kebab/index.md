---
lesson_name: Make a Kebab
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 441
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 442
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

### Make a kebab

Write a function that takes a sentence as input and converts it into kebab case. Kebab case is a naming convention where spaces are replaced with hyphens `"-"`, all letters are lowercase, and only alphabets and numbers are kept, while symbols are stripped off.

---

### Tests

<ul>
<li id="test-1"><code>make_kebab("Hello World")</code> should return <code>"hello-world"</code></li>
<li id="test-2"><code>make_kebab("Python Programming Language")</code> should return <code>"python-programming-language"</code></li>
<li id="test-3"><code>make_kebab("This Is a Sentence!")</code> should return <code>"this-is-a-sentence"</code></li>
<li id="test-4"><code>make_kebab("Coding Is Fun!!!")</code> should return <code>"coding-is-fun"</code></li>
<li id="test-5"><code>make_kebab("I Love Python*&amp;^%")</code> should return <code>"i-love-python"</code></li>
</ul>
