---
lesson_name: Sorting results with ORDER BY
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 500
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 501
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 502
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

## Sorting results with ORDER BY

So far, the rows we get back from a query come out in whatever order the database happens to store them in. The `ORDER BY` clause lets us control that order.

```sql
SELECT
    column_name
FROM
    table
ORDER BY
    column_name;
```

- `ORDER BY column_name`: Sorts the result by the given column, from smallest to largest (ascending) by default.

You can also sort by a column you are not even selecting, and you can sort by multiple columns by separating them with a comma:

```sql
SELECT
    first_name,
    last_name
FROM
    customers
ORDER BY
    last_name,
    first_name;
```

This sorts the rows by `last_name` first, and for rows that share the same `last_name`, sorts them by `first_name`.

---

### Exercise

Write a command that retrieves all columns from the `customers` table, sorted by `age` from youngest to oldest.

#### Tests

<ul>
<li id="test-1">The result has an <code>age</code> column.</li>
<li id="test-2">The rows are sorted by <code>age</code> from smallest to largest.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    customers
ORDER BY
    age;
```

</details>
