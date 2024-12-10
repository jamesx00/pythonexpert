---
lesson_name: Code Block in Python
code_editor: True
code_execution: True
adding_file_allowed: False
section: Python Functions
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 221
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 220
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

### Code blocks in Python

We can observe that there is an **indentation** under the function name when we define a new function. While indentation in other languages may be used for readability purposes, in Python, it plays a critical role in the code's operation.

Using whitespace or indentation to indent the code is a way to indicate to the code reader and the Python program that the code at this level belongs to the same group, or sometimes called the same **code block**. Each code block must have the same number of spaces or tabs, for example, the example below will use 4 spaces and 1 space for indentation.

```python
def say_hi(): # Block 1
    print("Hello World!") # Block 2
    print("How is it going?") # Block 2

def say_hi_2(): # Block 1
 print("Hello World!!") # Block 2
 print("How is it going??") # Block 2
```

However, in code blocks at the same level, not using the same number of spaces or tabs to indent the code will cause the program to fail with an error <span class="text-red-500">IndentationError: unexpected indent</span>. Therefore, it is important to pay attention to the code indentation in Python.

```python
def do_something(): # Block 1
    print("Do this") # Block 2
        print("Do that") # Block 2
```

<div class="alert-info text-sm">Modern code editors often have functions to help manage indentation, including online editors on our website. Everyone can use the <b>Tab</b> key to add 4 spaces, and sometimes the system will also automatically add spaces, such as when detecting a function definition. <br /><br />
Try typing the code example above in the editor and observe the automatic indentation.</div>

---

### Exercise

<ul>
<li id="test-1">Adjust the indentation in the function definition from 4 spaces to 2 spaces.</li>
</ul>
