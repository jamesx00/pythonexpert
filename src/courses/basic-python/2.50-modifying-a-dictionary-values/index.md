---
lesson_name: Modifying a Dictionary Values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 182
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 181
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

### Modifying dictionary values

You can also modify the value of a key by re-assigning it:

```python
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
}

my_dict["age"] = 26
print(my_dict["age"]) # 26
```

As you can see, the `my_dict["age"]` was 25 before we reassigned it to 26.

---

### Exercise

We have created a dictionary `job_position`. Change the value of the key **"experience_required"** to the value other than 5.

#### Tests

<ul>
<li id="test-1"><code>job_position["experience_required"]</code> should be any value other than <code>5</code></li>
<li id="test-2">Update the value using square brackets <code>[]</code></li>
</ul>
