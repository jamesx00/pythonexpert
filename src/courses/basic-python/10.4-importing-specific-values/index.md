---
lesson_name: Importing Specific Values
code_editor: True
code_execution: True
adding_file_allowed: True
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 452
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 454
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: greetings.py
        file_type: python
        id: 453
        is_closable: false
        is_edit_focus: false
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: greetings.py
    id: 1
    name: Python
---

### Importing specific values

To import specific values from a module, we use the `from` keyword followed by the module name, then the `import` keyword, and finally the specific values we want to import. Here's an example:

```python
from module_name import value_name
```

In this case, we are importing only the `value_name` from the module `module_name` module, instead of the entire module. We can then use the `value_name` in our code.

<div class="alert-danger text-sm">
We could also import all values by using the wildcard <code>*</code>, like so:
<code class="hljs language-python"><span class="hljs-keyword">from</span> module_name <span class="hljs-keyword">import</span> *
</code>. However, this is generally not recommended, as it can lead to name clashes and make the code harder to read and maintain, since we won't know from which module are the values coming from.
</div>

---

### Exercise

Update the import statement to import the function `greet` instead of importing the `greetings` module.

#### Tests

<ul>
<li id="test-1">Import <code>greet</code> function instead of <code>greetings</code> module</li>
<li id="test-2">Call the <code>greet("Jeff")</code> function</li>
</ul>
