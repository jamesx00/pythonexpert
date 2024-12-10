---
lesson_name: Negate a Boolean with not Keyword
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 211
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 212
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

### Reverse a boolean with not keyword

The `not` keyword in Python is a logical operator that reverses the boolean value of a condition.

For example, if we have a boolean expression that evaluates to `True`, we can use the `not` keyword to reverse it to `False`, and vice versa.

Here are some examples on how to use `not` keyword:

```python
print(not True) # Output: False

print(not 50 == 50) # Output: False

my_list = ["A", "B", "C", "D"]
print("A" not in my_list) # Output: False
print(not "A" in my_list) # Output: False
```

In the example above, `not True` is evaluated to `False`. And `not 50 == 50` is also `False`, as it is equivalent to `not True`.

In the list examples, we can use the keywords `not in` to get the opposite result of `in`. We can also add the keyword `not` before the entire expression as well.

---

### Exercise

Add the keyword `not` in the code to pass the tests

#### Tests

<ul>
<li id="test-1"><code>true</code> equals to <code>True</code></li>
<li id="test-2"><code>false</code> equals to <code>False</code></li>
<li id="test-3"><code>not_has_a</code> equals to <code>False</code></li>
<li id="test-4"><code>not_has_z</code> equals to <code>True</code></li>
<li id="test-5"><code>not_has_name</code> equals to <code>False</code></li>
<li id="test-6"><code>not_has_salary</code> equals to <code>True</code></li>
</ul>
