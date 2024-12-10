---
lesson_name: Importing Multiple Values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 455
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 457
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: greetings.py
        file_type: python
        id: 456
        is_closable: false
        is_edit_focus: false
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: greetings.py
    id: 1
    name: Python
---

### Importing multiple values

When working with modules in Python, it is common to import multiple values from a module into your current namespace.

Here's how to import multiple values in Python:

```python
from module_name import value1, value2, value3
```

In this example, we import the values `value1`, `value2` and `value3` from the `module_name` module. We can then use these values directly without referencing the module name.

---

### Exercise

Import functions `greet1()` and `greet2()` from `greetings` module and call both functions

#### Tests

<ul>
<li id="test-1">Import function <code>greet1()</code> from <code>greetings</code> module</li>
<li id="test-2">Import function <code>greet2()</code> from <code>greetings</code> module</li>
<li id="test-3">Call <code>greet1("Leena")</code></li>
<li id="test-4">Call <code>greet2("Dillan")</code></li>
</ul>
