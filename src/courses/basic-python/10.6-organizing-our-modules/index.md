---
lesson_name: Organizing Our Modules
code_editor: True
code_execution: True
adding_file_allowed: True
file_groups:
  - common: false
    files:
      - file_name: greetings.py
        file_type: python
        id: 70
        is_closable: true
        is_edit_focus: false
        is_editable: false
        is_hidden: false
        is_main: false
        is_test_file: false
        source: greetings.py
      - file_name: main.py
        file_type: python
        id: 69
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 461
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

### Organizing Our Modules

After learning how to create a module in a file within the same directory as our Python script, we may want to organize our code better by creating a module in a folder. This allows us to group related functionality together and avoid cluttering our main code file.

Here are the steps to create a module inside a folder from our previous example:

1. Create an empty file named **greetings/\_\_init\_\_.py**. This will create a folder named **greetings** and a new file **\_\_init\_\_.py**. The file structure now looks like this:

   ```bash
   .
   ├── main.py # Our main file
   ├── greetings.py
   └── greetings # A module folder
       └── __init__.py
   ```

   <div class="alert-info text-sm">
   The <code>__init__.py</code> file is required when you want to treat a directory as a package and import modules from it. When Python imports a package, it looks for the <code>__init__.py</code> file in the directory, and if it's present, it knows that the directory is a package and can be imported. If the <code>__init__.py</code> file is missing, Python will not recognize the directory as a package and will not be able to import modules from it.

   In Python 3.3 and later, the <code>\_\_init\_\_.py</code> file is no longer strictly required for a package. However, it's still a good practice to include it, as it makes the package more explicit and easier to understand for other developers.
   </div>

2. Create another file named **greetings/functions.py**, and copy the content of the file **greetings.py** into the new file we just created.

   ```bash
   .
   ├── main.py # Our main file
   ├── greetings.py
   └── greetings # A module folder
       ├── __init__.py
       └── functions.py
   ```

3. Now that we have both the file **greetings.py** and the module folder **greetings**, we need to remove the file **greetings.py** to avoid naming conflict and to make sure that whenever we import the module with `import greetings` or `from greetings import ...`, Python will look inside the folder instead of the **greetings.py** file. Remove the file by selecting the file, then click `x` to the right of the file name.

   ```bash
   .
   ├── main.py # Our main file
   └── greetings # A module folder
       ├── __init__.py
       └── functions.py
   ```

4. Now, we can use this module in our Python script by importing it. Update the code in **main.py** to import and use the `greet()` function in the new file we created:

   ```python
   from greetings.functions import greet

   greet("Alice") # Output: Hello Alice!
   ```

   You could also use another import syntax as well

   ```python
   from greetings import functions

   functions.greet("Alice") # Output: Hello Alice!
   ```

---

### Exercise

Follow the instructions in this lesson.

#### Tests

<ul>
<li id="test-1">A new file <code>greetings/__init__.py</code> is created</li>
<li id="test-2">A new file <code>greetings/functions.py</code> is created</li>
<li id="test-3">Copy the function <code>greet()</code> from <code>greetings.py</code> to <code>greetings/functions.py</code></li>
<li id="test-4">Remove the file <code>greetings.py</code></li>
<li id="test-5">Update the import path in the <code>main.py</code> file</li>
<li id="test-6">Call the function greet with the name <code>"Alice"</code></li>
</ul>
