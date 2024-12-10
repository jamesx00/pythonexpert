---
lesson_name: Iterate with While Loops
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 30
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 248
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

### Iterate with while loops

A `while` loop in Python is a type of loop that repeats a block of code as long as a certain condition is `True`. It has the following syntax:

```python
while condition:
    # code to be executed while the condition is true
```

Or we can use the keyword `else` as well. For example:

```python
while condition:
    # code to be executed while the condition is true
else:
    # optional code to be executed when the condition is false
```

Here, **condition** is the expression that is evaluated before each iteration of the loop. If the condition is `True`, then the code inside the loop is executed. This process is repeated until the condition becomes `False`, at which point the program continues executing after the loop. The _optional_ `else` block is executed after the loop finishes if the condition becomes False.

Here's an example of a while loop that uses the else block:

```python
num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("Finished counting!")
```

```bash
Output:
1
2
3
4
5
Finished counting!
```

In this example, the condition `num <= 5` is evaluated before each iteration of the loop. As long as `num` is less than or equal to 5, the loop continues to execute, printing the value of num and incrementing it by 1. When num becomes 6 and the condition becomes false, the program executes the else block and prints `"Finished counting!"`.

### Infinite Loop

It's important to be careful when writing while loops to avoid creating **infinite loops**, which are loops that never terminate because the condition is always `True`. Here's an example of an infinite loop:

```python
while True:
    print("Hello")
```

<div class="alert-warning text-sm">
You can copy the above code to run on an online editor to see the results, but the system will stop working before it uses resources and causes a failure.
</div>

This while loop has a condition of `True`, which is always true, so the loop will continue to execute indefinitely, printing `"Hello"` over and over again. To stop an infinite loop, you can press `Ctrl + C` to interrupt the program or modify the code to include a condition that will eventually become false.

---

### Exercise

<ul>
<li id="test-1">Print any message 5 times using the <code>while</code> loop and <code>print()</code> function</li>
</ul>
