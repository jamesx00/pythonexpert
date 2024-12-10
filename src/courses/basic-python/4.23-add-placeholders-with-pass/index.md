---
lesson_name: Add Placeholders with Pass
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 277
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 276
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

### Add placeholders with pass

In Python, the `pass` statement is a placeholder statement that does nothing. It is used when a statement is required syntactically but you don't want to execute any code. The `pass` statement is typically used as a placeholder for code that will be implemented later.

One common use case for the `pass` statement is to create empty code blocks:

In Python, code blocks are defined using indentation. However, sometimes you may need to define a block without any statements. In such cases, you can use the `pass` statement to indicate an empty code block. This is often used as a placeholder when defining functions, classes, or conditional statements that will be implemented later.

```python
def my_function():
    pass  # Placeholder for the function body

if condition:
    pass  # Placeholder for the if statement block
```

---

### Exercise

Add `pass` statement inside the `for` loop so that the program can run without any syntax errors.

#### Tests

<ul>
<li id="test-1">Use <code>pass</code> statement in the code</li>
<li id="test-2">The program runs without any errors</li>
</ul>
