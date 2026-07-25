---
lesson_name: Selecting unique values with DISTINCT
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 509
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 510
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 511
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

## Selecting unique values with DISTINCT

A table often has repeated values in a column. The `DISTINCT` keyword removes duplicate rows from the result, keeping only unique values:

```sql
SELECT DISTINCT
    column_name
FROM
    table;
```

For example, our `customers` table has a `gender` column that only ever contains `M` or `F`. Instead of getting the value once per customer, `DISTINCT` gives us each unique value once:

```sql
SELECT DISTINCT
    gender
FROM
    customers;
```

`DISTINCT` applies to the whole row being selected, so if you select multiple columns, only rows where **all** selected columns match together are treated as duplicates.

---

### Exercise

We have already created a table `products` with the columns `id`, `name`, `category`, and `price`. Write a command that retrieves the distinct list of `category` values from `products`.

#### Tests

<ul>
<li id="test-1">The result has a <code>category</code> column.</li>
<li id="test-2">The result contains each category value exactly once, with no duplicates.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT DISTINCT
    category
FROM
    products;
```

</details>
