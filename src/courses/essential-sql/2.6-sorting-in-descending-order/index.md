---
lesson_name: Sorting in descending order
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 503
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 504
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 505
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

## Sorting in descending order

By default, `ORDER BY` sorts from smallest to largest. To reverse the order, add the `DESC` keyword after the column name:

```sql
SELECT
    column_name
FROM
    table
ORDER BY
    column_name DESC;
```

If you want to be explicit about the default ascending order, you can add `ASC` instead, although it is optional since it is the default:

```sql
SELECT
    column_name
FROM
    table
ORDER BY
    column_name ASC;
```

You can even mix directions when sorting by multiple columns:

```sql
SELECT
    first_name,
    last_name
FROM
    customers
ORDER BY
    last_name DESC,
    first_name ASC;
```

---

### Exercise

Write a command that retrieves all columns from the `customers` table, sorted by `age` from oldest to youngest.

#### Tests

<ul>
<li id="test-1">The result has an <code>age</code> column.</li>
<li id="test-2">The rows are sorted by <code>age</code> from largest to smallest.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    customers
ORDER BY
    age DESC;
```

</details>
