---
lesson_name: Lambda Functions
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 38
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 322
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

### Lambda function

In the previous lesson, when we defined a function, those functions would have their own names, which allows us to call the function by its name. For example, the function below has the name **say_hello**:

```python
def say_hello(name):
    print(f"Hello {name}")
```

However, in some cases, we may want to define a function to be used only once, and creating a named function would take up space in the **namespace** or the area for naming different things (we cannot use the same name for variables and functions, for example). In this case, we can use the `lambda` keyword to create a function. The syntax for writing a function using lambda is:

```python
lambda arguments: expression
```

Functions created with the lambda keyword can accept an unlimited number of arguments but can only have one expression, which will be the statement that returns a value from the function. For example, the following example can be written using either def or lambda, and both functions will work in the same way:

```python
def double(number):
    return number * 2
```

```python
double = lambda number: number * 2
```

The expression following the `:` is the statement of the function that will return a value to us, and we can call the function normally, such as:

```python
double = lambda number: number * 2

print(double(10))
```

We can define functions using the lambda keyword in various ways, such as the examples below:

```python
my_func_0 = lambda: print("Hello there!")
double = lambda number: number * 2
multiply = lambda num1, num2: num1 * num2
test_func = lambda x, y, z: x + y + z
```

In general, we use lambda functions when we want to create a simple function that performs non-complex tasks. If we want to create a function that performs complex tasks, we can use the def keyword to create a function as usual.

---

### Tests

<ul>
<li id="test-1">Write a lambda function that returns the input number multiplied by 5 and assign it to the variable <code>multiply_by_five</code></li>
<li id="test-2"><code>multiply_by_five(2)</code> should return <code>10</code></li>
<li id="test-3"><code>multiply_by_five(10)</code> should return <code>50</code></li>
</ul>
