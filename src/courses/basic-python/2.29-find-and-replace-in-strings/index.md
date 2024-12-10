---
lesson_name: Find and Replace in Strings
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 146
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 147
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

### Find and replace a value in a string

You can use the function `replace()` to find and replace a specific value in a string. Here's how you can call this function:

```python
string.replace(oldvalue, newvalue, count)
```

The **oldvalue** is the value you want to replace, and the **newvalue** is the value you want to replace the **oldvalue** with. And **count** tells Python how many times do you want to find and replace the **oldvalue**. If you leave out the **count**, Python will replace all the occurrences in the string.

For example:

```python
sentence = "Python is a good programming language"
new_sentence = sentence.replace("good", "great")
print(new_sentence) # Python is a great programming language

sentence_2 = "Ant Bird Bird Cat"
new_sentence_2 = sentence_2.replace("Bird", "Dog", 1) # Only replace Bird once
print(new_sentence_2) # Ant Dog Bird Cat
```

---

### Exercise

<ul>
<li id="test-1">Replace all occurrences of <strong>A</strong> with <strong>_</strong> in the variable <code>sentence</code> and assign it to <code>new_sentence</code></li>
<li id="test-2">Use the function <code>replace()</code></li>
<li id="test-3">Do not change the first line of the code</li>
</ul>
