---
lesson_name: Looping Through Lists with Zip
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 268
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 267
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

### Looping through lists with zip

We can loop through multiple sequences, such as strings, lists, or tuples with `zip()`.

Here's what happens when you call the `zip()` function with multiple lists:

```python
list_a = [1,2,3]
list_b = [4,5,6]
print(list(zip(list_a, list_b)))
# [(1, 4), (2, 5), (3, 6)]
```

From the example above, we call the function `zip()` with two lists. The function then returns us a list of tuples, each tuple contains two elements from each list.

With this knowledge, we can now loop through multiple lists with `for` loop, `zip()`, and data unpacking:

```python
names = ['John', 'Alice', 'Bob']
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

```bash
Output:
John is 30 years old
Alice is 25 years old
Bob is 35 years old
```

We can also loop more than 3 lists at the same time as well:

```python
names = ['John', 'Alice', 'Bob']
ages = [30, 25, 35]
countries = ['USA', 'Canada', 'UK']

combined = zip(names, ages, countries)
for name, age, country in combined:
    print(name, age, country)
```

---

### Exercise

Combine the values in the lists `students` and `scores` into a new list `results`.

#### Tests

<ul>
<li id="test-1">Variable <code>results</code> should be <code>['Rhonda Hart: 60', 'Ernest Aguirre: 70', 'Sean Jackson: 80']</code></li>
<li id="test-2">Use <code>zip()</code> function</li>
</ul>

#### Hints

Each element in `results` should be a string in the format `"{student}: {score}"`. For example, `"Rhonda Hart: 60"`.
