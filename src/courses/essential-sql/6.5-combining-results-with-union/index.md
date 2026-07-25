---
lesson_name: Combining results with UNION
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 912
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 913
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 914
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

## Combining results with UNION

Every join we've looked at so far combines tables **side by side**, adding columns from a second table onto each row. `UNION` does something different: it stacks the results of two `SELECT` statements **on top of each other**, as long as both statements return the same number of columns.

```sql
SELECT
    column_1
FROM
    table_1
WHERE
    condition_1
UNION
SELECT
    column_1
FROM
    table_2
WHERE
    condition_2;
```

- Both `SELECT` statements must return the same number of columns.
- `UNION` combines the rows from both statements into a single result, and removes any duplicate rows.
- If you want to keep duplicates instead of removing them, use `UNION ALL`.

### Example

```sql
SELECT
    name
FROM
    products
WHERE
    category = 'Home'
UNION
SELECT
    name
FROM
    products
WHERE
    category = 'Office';
```

Result:

```bash
+-------------+
|     name    |
+-------------+
|  Coffee Mug |
|  Desk Lamp  |
|   Notebook  |
|   Backpack  |
+-------------+
```

This gets us every `Home` product stacked together with every `Office` product, as a single column of names. Note that this particular example could also be written with `WHERE category IN ('Home', 'Office')`, since both `SELECT` statements pull from the same table and column, `UNION` is more useful once the two statements pull from different tables or different sets of columns, but the mechanics are easiest to see when the columns line up like this.

---

### Exercise

Write a query that returns the `name` of every product in the `'Electronics'` category, `UNION`-ed with the `name` of every product in the `'Fitness'` category.

<ul>
<li id="test-1">The result has a <code>name</code> column.</li>
<li id="test-2">The result contains exactly the products from the <code>Electronics</code> and <code>Fitness</code> categories, with no duplicates.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    name
FROM
    products
WHERE
    category = 'Electronics'
UNION
SELECT
    name
FROM
    products
WHERE
    category = 'Fitness';
```

</details>
