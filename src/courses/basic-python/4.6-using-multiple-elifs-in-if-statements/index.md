---
lesson_name: Using Multiple Elifs in If Statements
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 242
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 241
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

### Using multiple elifs in if statements

You can use multiple `elif` statements in an if block to specify more than two possible conditions to be checked. The first `elif` statement whose condition is `True` executes its block of code, and the rest of the elif statements are skipped.

Here's an example:

```python
def get_age_description(age):
    if age < 18:
        return "You are not yet an adult."
    elif age >= 18 and age < 21:
        return "You are an adult, but you cannot drink."
    elif age >= 21 and age < 65:
        return "You are an adult and can drink."
    elif age >= 65:
        return "You are a senior citizen."

print(get_age_description(25)) # Output: You are an adult and can drink.
```

In this example, we use multiple elif statements to check if someone is an adult, if they can drink alcohol, or if they are a senior citizen.

---

### Exercise

- Use an `if-ellf-else` statement so that the function `get_grade()` returns the correct value:
  - If `score` is greather than or equal to 90, returns `"A"`.
  - If `score` is greather than or equal to 80, returns `"B"`.
  - If `score` is greather than or equal to 70, returns `"C"`.
  - If `score` is greather than or equal to 60, returns `"D"`.
  - For any other values of `score`, returns `"F"`.

#### Tests

<ul>
<li id="test-1"><code>get_grade(90)</code> should returns <code>"A"</code>.</li>
<li id="test-2"><code>get_grade(80)</code> should returns <code>"B"</code>.</li>
<li id="test-3"><code>get_grade(70)</code> should returns <code>"C"</code>.</li>
<li id="test-4"><code>get_grade(60)</code> should returns <code>"D"</code>.</li>
<li id="test-5"><code>get_grade(50)</code> should returns <code>"F"</code>.</li>
</ul>
