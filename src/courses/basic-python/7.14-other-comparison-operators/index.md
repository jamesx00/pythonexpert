---
lesson_name: Other Comparison Operators
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 363
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 362
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

### Other comparison operators

Aside from equality operators, we can implement how our objects behave with other comparison operators. Here's a list of operators and their corresponding methods:

| Operator                      | Method                |
| ----------------------------- | --------------------- |
| `==` equal to                 | `__eq__(self, other)` |
| `<` less than                 | `__lt__(self, other)` |
| `<=` less than or equal to    | `__le__(self, other)` |
| `>` greater than              | `__gt__(self, other)` |
| `>=` greater than or equal to | `__ge__(self, other)` |

---

### Exercise

- Implement all types of comparison operators for our `MyStr` class.

#### Tests

<ul>
<li id="test-1"><code>MyStr("1") == MyStr("1")</code> is <code>True</code></li>
<li id="test-2"><code>MyStr("1") != MyStr("1")</code> is <code>False</code></li>
<li id="test-3"><code>MyStr("1") &lt; MyStr("1")</code> is <code>False</code></li>
<li id="test-4"><code>MyStr("1") &gt; MyStr("1")</code> is <code>False</code></li>
<li id="test-5"><code>MyStr("1") &lt;= MyStr("1")</code> is <code>True</code></li>
<li id="test-6"><code>MyStr("1") &gt;= MyStr("1")</code> is <code>True</code></li>
</ul>
