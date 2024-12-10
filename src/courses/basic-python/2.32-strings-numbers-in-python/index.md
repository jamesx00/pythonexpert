---
lesson_name: Strings & Numbers in Python
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 52
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 150
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

## Difference Between Strings and Numbers

In Python, there is a fundamental difference between numbers and number strings. Numbers are a numeric data type that can be used in mathematical calculations, while number strings are simply strings of characters that happen to contain digits.

Let's take a look at some examples to see the difference in action.

```python
# Examples of numbers
x = 5
y = 3.14
z = -10

# Examples of number strings
a = "123"
b = "-4.56"
c = "1.2e-3"
```

In this example, `x`, `y`, and `z` are all numeric variables. They can be used in mathematical calculations, such as addition, subtraction, multiplication, and division. For example:

```python
result = x + y  # result is now 8.14
```

On the other hand, `a`, `b`, and `c` are all number strings. They are not numeric data types, so they **cannot** be used in mathematical calculations directly. If you try to perform mathematical operations on number and string, Python will raise a `TypeError`.

```python
result = a + x # This will raise a TypeError
result_2 = a + b # This will give a new string "123-4.56" instead
```

### Converting strings to numbers

To perform mathematical operations on number strings, you first need to convert them to numeric data types using functions like `int()`, `float()`, or `complex()`. For example:

```python
i = int(a)  # i is now the numeric value 123
j = float(b)  # j is now the numeric value -4.56
k = complex(c)  # k is now the complex value (1.2e-3+0j)
```

### Converting other data types to strings

You can convert other data types, such as numbers or booleans, to strings using the `str()` function. For example:

```python
my_number = 42
my_string = str(my_number)
print(type(my_string)) # Output <class 'str'>
```

You can access individual characters in a string using indexing, and you can extract substrings using slicing. You can't do this with numbers, since they don't have individual "characters" to extract. For example:

```python
my_string = "Hello, world!"
print(my_string[0])   # "H"
print(my_string[7:12])  # "world"
```

In general, it's important to keep in mind the difference between numbers and number strings in Python. Make sure to use the appropriate data type for the task at hand, and convert between data types as necessary.

---

### Exercise

<ul>
<li id="test-1">Use the converting function <code>int()</code> or <code>float()</code> to change the value of <code>string_number</code> so that the <code>result</code> is equal to <code>40</code></li>
<li id="test-2">Do not change the first two lines of code</li>
</ul>
