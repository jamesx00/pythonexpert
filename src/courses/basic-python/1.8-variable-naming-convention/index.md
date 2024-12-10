---
lesson_name: Variable Naming Convention
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 88
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 89
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Naming Convention for Variables

The naming convention for variables may differ in each programming language. In Python, variables can have English letters, both lowercase and uppercase `a-z` `A-Z`, numbers `0-9`, and underscores `_`. However, variable names cannot start with a number. Examples of valid variable names are:

```python
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
```

Examples of **_invalid_** variable name:

```python
1099_failed = False
```

<div class="alert-info text-sm">
There are four naming conventions for variables:<br />
<ol>
<li><b>Snake Case</b>, which uses an underscore _ between words, such as student_name, company_phone_number</li>
<li><b>Kebab Case</b>, which is similar to Snake Case but uses a hyphen - instead of an underscore _, such as student-name, company-phone-number</li>
<li><b>Camel Case</b>, which uses the first letter of each word capitalized, except for the first word, such as studentName, companyPhoneNumber</li>
<li><b>Pascal Case</b>, which is similar to Camel Case but starts with a capitalized first letter for the first word, such as StudentName, CompanyPhoneNumber</li>
</ol>

In Python, snake case is a convention used for naming variables.

</div>

---

### Exercise

<ul>
<li id="test-1">Change the variable name from <code>1099_failed</code> to <code>year</code>.</li>
</ul>
