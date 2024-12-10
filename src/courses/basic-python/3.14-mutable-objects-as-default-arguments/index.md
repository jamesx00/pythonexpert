---
lesson_name: Mutable Objects as Default Arguments
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 418
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 419
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

### Mutable objects as default arguments

A few lessons ago, we created a function with default arguments. However, something strange happens when we use mutable objects, such as **dict**s or **list**s as default arguments.

Here's an example:

```python
def add_key_to_dict(key, value, the_dict={}):
    the_dict[key] = value
    return the_dict

new_object = add_key_to_dict("year", 2050)
another_object = add_key_to_dict("color", "yellow")
print(new_object) # {'year': 2050, 'color': 'yellow'}
print(another_object) # {'year': 2050, 'color': 'yellow'}
```

We would expect `new_object` and `another_object` to be different objects, but they are the same object.

In Python functions, **the default values are initialized only once when the function is defined. They are not created every time the function is called.** Therefore, `the_dict` in the example above is the same object every time we call the function. And when we call `the_dict[key] = value`, we operate on the same dictionary.

To set a mutable object as a default argument, set the value to `None` and use the `if` statement to check if the value is `None`. Like so:

```python
def add_key_to_dict(key, value, the_dict=None):
    if the_dict is None:
        the_dict = {}
    the_dict[key] = value
    return the_dict

new_object = add_key_to_dict("year", 2050)
another_object = add_key_to_dict("color", "yellow")
print(new_object) # {'year': 2050}
print(another_object) # {'color': 'yellow'}
```

<div class="alert-info text-sm">
Any value other than <code>None</code> will also work, but <code>None</code> is a common choice.
</div>

We can take a step further to avoid causing side effects altogether:

```python
def add_key_to_dict(key, value, the_dict=None):
    if the_dict is None:
        result = {}
    else:
        result = the_dict.copy()
    result[key] = value
    return result
```

---

### Exercise

Update the default argument in the function `add_list_item()`

#### Tests

<ul>
<li id="test-1"><code>add_list_item(3, [1, 2])</code> should return <code>[1, 2, 3]</code></li>
<li id="test-2"><code>add_list_item(1)</code> should return <code>[1]</code>, and subsequent <code>add_list_item(2)</code> should return <code>[2]</code></li>
</ul>
