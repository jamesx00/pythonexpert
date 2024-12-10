---
lesson_name: Variable Scope in Python
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 36
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 232
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

### Variable scope in Python

Every variable in Python has its own scope, which determines where the variable can be accessed in the program. In Python, there are four scopes in total, which are commonly abbreviated as **LEGB**, standing for Local, Enclosing, Global, and Built-in.

### Local Scope

When we define a function, the variables specified within the function can only be accessed within that function and cannot be accessed or modified from outside the function. For example, in the following code snippet, if we try to access the variable `name outside` of the function `print_name()`, we will get an error saying that the name is not defined.

```python
def print_name():
    name = "James"
    print(f"My name is {name}")

print_name() # My name is James
print(f"My name is {name}") # NameError: name 'name' is not defined
```

### Enclosing Scope

If we define a function inside another function, the variable defined inside the inner function cannot be accessed from outside. For example, in the following code, the outer function cannot access the `inner_number` variable. However, the inner function can access both `outer_number` and `inner_number` variables.

```python
def outer():
    outer_number = 5
    def inner():
        inner_number = 10
        print(outer_number)
        print(inner_number)
    inner()
    print(inner_number)

outer()

# 5
# 10
# NameError: name 'inner_number' is not defined
```

### Global Scope

When a variable is defined or assigned a value outside of a function, those variables are considered global variables and can be accessed from anywhere in the program.

```python
name = "James"

def print_name():
    print(f"Hello {name}")
```

### Built-in Scope

Built-in scope is the widest scope and consists of various keywords used in the Python language without the need for any prior definition.

|         |       |          |          |        |
| ------- | ----- | -------- | -------- | ------ |
| True    | False | None     | def      | import |
| if      | elif  | else     | try      | except |
| finally | pass  | continue | break    | import |
| async   | await | class    | is       | and    |
| or      | not   | return   | raise    | yield  |
| lambda  | as    | global   | nonlocal | in     |
| for     | del   | from     | while    | assert |

### The LEGB rule

When we call a function that uses variables, the program will look for those variables in the local scope first. If it does not find the variables in that scope, it will then look for them in wider scopes. For example, in the previous example functions `inner()` and `outer()`, Python would first look for the variable within the local scope of inner before looking for it in the scope of outer.

### The `global` and `nonlocal` keywords

When a variable is defined within a function, it automatically becomes a local variable in that function's scope. However, we can change the scope of those variables ourselves if we want to. For example, in the following example, when we define the variable `global_number()` and use the `print()` function at the end, instead of displaying 20, it displays 10. This is because when we are inside the function `change_global_number()`, Python creates another variable in the local scope, separate from the global_number outside the function.

```python
global_number = 10

def change_global_number(new_number):
    global_number = new_number
    print(global_number)

change_global_number(20) # Output: 20
print(global_number) # Output: 10
```

If we want a function to use a variable in the global scope, we can use the keyword `global` followed by the variable name within the function.

```python
global_number = 10

def change_global_number(new_number):
    global global_number
    global_number = new_number
    print(global_number)

change_global_number(20) # Output: 20
print(global_number) # Output: 20
```

While the `global` keyword is used to access variables in the global scope, we can use the `nonlocal` keyword to access variables in a higher-level scope. For example, in the previous example of the inner and outer functions, we can force the inner function to use variables in the scope of the outer function.

```python
def outer():
    outer_number = 5
    def inner():
        nonlocal outer_number
        outer_number = 10
        print(outer_number)
    inner()
    print(outer_number)

outer()
```

---

### Exercise

Add a `global` keyword inside the function `change_global_number` to use the variable `global_number` in the global scope.

#### Tests

<ul>
<li id="test-1">Variable <code>global_number</code> should be <code>30</code> after calling the function <code>change_global_number()</code></li>
<li id="test-2">Add your code only on line 5</li>
</ul>
