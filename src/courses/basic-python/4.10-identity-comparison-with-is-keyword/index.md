---
lesson_name: Identity Comparison with Is Keyword
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 247
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 246
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

### Identity comparison with is keyword

The `is` keyword is used for object identity comparison. Whenever we create a value in Python, we created an **object** that is stored in the memory, and the keyword `is` checks if two objects are the same object by comparing their memory locations, whereas the `==` operator compares the values of the objects.

For example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True
print(a is b)  # False

print(a == c)  # True
print(a is c)  # True
```

In the above example, `a` and `b` have the same values but they point to different memory locations because they were created separately, so `a is b` returns `False`. On the other hand, `a` and `c` both point to the same memory location, so `a is c` returns `True`.

It's important to note that `is` keyword should be used only for comparing with `None`, and sometimes `True` and `False` if you want to check if the value is the `True` or `False` objects. For example:

```python
a = True
b = 50

print(b == True) # True
print(b is True) # False
print(a is True) # True
```

There are cases where `is` can be useful for comparing object identities. For instance, when we want to check if a variable has been assigned any value, we can use `is None` instead of `== None`. Here is an example:

```python
my_var = None

if my_var is None:
    print("my_var has no value")
else:
    print("my_var has a value")
```

---

### Exercise

Fix the code inside the function `is_true_or_false()` to check if the variable `value` is really a boolean `True` or `False`.

#### Tests

<ul>
<li id="test-1"><code>is_true_or_false(True)</code> should return <code>True</code></li>
<li id="test-2"><code>is_true_or_false(False)</code> should return <code>True</code></li>
<li id="test-3"><code>is_true_or_false(None)</code> should return <code>False</code></li>
<li id="test-4"><code>is_true_or_false(1)</code> should return <code>False</code></li>
<li id="test-5"><code>is_true_or_false(0)</code> should return <code>False</code></li>
<li id="test-6"><code>is_true_or_false([1, 2, 3])</code> should return <code>False</code></li>
<li id="test-7"><code>is_true_or_false([])</code> should return <code>False</code></li>
</ul>
