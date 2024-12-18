---
lesson_name: Select multiple columns
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 474
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 475
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 476
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: SQL
---

## Select multiple columns

Now that we know how to select one column from a table, here's the syntax to select multiple columns:

```sql
SELECT column1, column2 FROM table;
```

- `column1, column2`: Specify the columns you want to retrieve, separated by a comma `,`, or use `*` to select all columns. Notice that there is no comma after the last column.
- `table`: Specifies the table from which to retrieve the data.

---

### Exercise

We have already created a table `customers` with the columns `first_name`, `last_name`, `age`, and `gender`. Write a command to retrieve data from `customers` table with all columns.

#### Tests

<ul>
<li id="test-1">The result has <code>first_name</code> column.</li>
<li id="test-2">The result has <code>last_name</code> column.</li>
<li id="test-3">The result has <code>age</code> column.</li>
<li id="test-4">The result has <code>gender</code> column.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT * FROM customers;
```

```sql
SELECT first_name, last_name, age, gender FROM customers;
```

</details>
