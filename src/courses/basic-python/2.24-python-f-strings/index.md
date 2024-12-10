---
lesson_name: Python f Strings
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 136
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 137
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

## Python f-strings

In Python, an **f-string** is a string that allows us to write additional code inside a string. An f-string is denoted by an **f** or **F** character at the beginning of a string. We can then use the `{}` to inject a variable or code into the string.

For example, instead of writing this:

```python
name = "James"
sentence = "My name is " + name
print(sentence) # output: My name is James
```

We can use f-string to print the sentence, like so:

```python
name = "James"
sentence = f"My name is {name}"
print(sentence) # output: My name is James
```

We can also use any expression within the `{}` as well.

```python
sentence = f"The total of 20 + 20 is {20 + 20}"
print(sentence) # output: The total of 20 + 20 is 40
```

---

### Exercise

<ul>
<li id="test-1"><code>sentence</code> should be <code>"Python is an amazing programming language."</code></li>
<li id="test-2"><code>sentence</code> is assigned with <strong>f-string</strong></li>
</ul>
