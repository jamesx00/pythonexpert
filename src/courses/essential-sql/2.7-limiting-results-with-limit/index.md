---
lesson_name: Limiting results with LIMIT
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 506
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 507
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 508
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

## Limiting results with LIMIT

Sometimes a table has far more rows than you need. The `LIMIT` clause caps the number of rows a query returns:

```sql
SELECT
    column_name
FROM
    table
LIMIT
    number;
```

- `number`: The maximum number of rows to return.

`LIMIT` is commonly combined with `ORDER BY` to answer questions like "who are the 3 oldest customers?":

```sql
SELECT
    first_name,
    last_name
FROM
    customers
ORDER BY
    age DESC
LIMIT
    3;
```

Without `ORDER BY`, `LIMIT` just returns however many rows the database happens to return first, which is not guaranteed to mean anything.

---

### Exercise

Write a command that retrieves the `first_name` and `age` columns from `customers`, sorted by `age` from oldest to youngest, and returns only the oldest **3** customers.

#### Tests

<ul>
<li id="test-1">The result has an <code>age</code> column.</li>
<li id="test-2">The result contains exactly 3 rows.</li>
<li id="test-3">The rows contain the 3 oldest customers, sorted from oldest to youngest.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    first_name,
    age
FROM
    customers
ORDER BY
    age DESC
LIMIT
    3;
```

</details>
