---
lesson_name: Exit The Loop with Break
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 273
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 272
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

### Exit the loop with break

In Python, the `break` statement is used to prematurely exit a loop. When encountered within a loop, the `break` statement immediately terminates the loop and transfers the program execution to the next statement after the loop.

Here's an example of using `break` to stop a for loop:

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

print("Loop finished")
```

In this example, the loop iterates over the `fruits` list. When the `fruit` variable becomes equal to `"cherry"`, the `break` statement is encountered, and the loop is exited. As a result, only `"apple"` and `"banana"` will be printed, and the program execution will continue with the statement after the loop, which is `print("Loop finished")`.

The output of the above code will be:

```bash
apple
banana
Loop finished
```

### Using with while loops

We can use `break` statements with `while` loops as well. In the example below, we use the `break` statement to stop the execution of the `while` loop when `x` equals `3`.

```python
x = 0
while True:
    print(f"The number is {x}")
    if x == 3:
        break
    x = x + 1
print("This is called after the loop")
```

```bash
Output
The number is 0
The number is 1
The number is 2
The number is 3
This is called after the loop
```

---

### Exercise

<ul>
<li id="test-1">Use <code>break</code> to stop the loop when the value <code>number</code> is equal to <code>5</code>, so that the function <code>print()</code> is called 5 times.</li>
</ul>
