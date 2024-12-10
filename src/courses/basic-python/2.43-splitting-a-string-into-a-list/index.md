---
lesson_name: Splitting a String into a List
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 172
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 171
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

### Split a string into a list

In Python, you can split a string into a list of substrings using the split() method. The `split()` method takes an optional separator as an argument, which is used to split the string into substrings.

If you do not specify the separator, it will default to a space character, like so:

```python
text = "Hello World, this is a test"
words = text.split()
print(words) # ['Hello', 'World,', 'this', 'is', 'a', 'test']
```

However, you can also specify a different separator to use when splitting the string. For example:

```python
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits) # ['apple', 'banana', 'orange']
```

---

### Exercise

<ul>
<li id="test-1">Change the argument inside the function <code>split()</code> so that the variable <code>countries</code> is a list of country names <code>['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Peru', 'France', 'Germany', 'Italy', 'Spain']</code>. Make sure to include both the comma and the trailing space to split the text</li>
<li id="test-2">Do not change the first line of code</li>
</ul>
