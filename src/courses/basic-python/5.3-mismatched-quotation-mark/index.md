---
lesson_name: Mismatched Quotation Mark
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 331
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 330
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

### Mismatched quotation mark

Python supports both single `'` and double `"` quotation marks for representing strings. It is important to use matching quotation marks to define string literals correctly.

Mismatched quotation mark errors occur when the opening and closing quotation marks in a string literal do not match. Python interprets the mismatched quotation marks as a syntax error and raises a `SyntaxError`.

For example, this will cause an error, because we use a single quotation mark at the beginning, but use a double quotation mark at the end:

```python
sentence = 'Hello World!"
```

If you need to include the same type of quotation mark within a string, use an escape character `\` before the quotation mark to indicate that it is part of the string and not the closing delimiter.

For example:

```python
sentence = 'I\'m doing great, thanks!'
```

---

### Exercise

- Fix the code so that it uses the correct quotation mark to define the string.
- Make sure the quotation mark(s) are escaped correctly.

#### Tests

<ul>
<li id="test-1">Variable <code>message</code> should be the sentence <code>He said, "Don't forget to bring your umbrella!"</code></li>
</ul>
