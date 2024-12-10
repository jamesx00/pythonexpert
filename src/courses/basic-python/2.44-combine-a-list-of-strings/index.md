---
lesson_name: Combine a list of strings
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 174
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 173
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

### Combine a list of strings into one string

We can combine a list of strings into a single string using the `join()` method, which is the opposite of the method `split()` we just learned about. This method takes a sequence (e.g., a list) of strings and concatenates them using the specified separator.

For example, here's how you can combine a list of words into a string with a space in between each word:

```python
words = ['Hello', 'world', '!']
sentence = ' '.join(words)
print(sentence)
```

---

### Exercise

Use the method `join()` to combine a list of words `words` into a new variable `sentence` with a single space between each word.

#### Tests

<ul>
<li id="test-1">Variable <code>sentence</code> should be <code>"banana chocolate computer umbrella guitar"</code></li>
<li id="test-2">Use the function <code>join()</code></li>
<li id="test-3">Do not change the first line of the code</li>
</ul>
