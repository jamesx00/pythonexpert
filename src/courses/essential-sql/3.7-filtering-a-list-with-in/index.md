---
lesson_name: Filtering a list with IN
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 618
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 619
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 620
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

## Filtering a list with IN

Checking a column against several possible values with `OR` gets repetitive fast. The `IN` keyword lets you list all the values you want to match in one place.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    column_name IN (value_1, value_2, value_3);
```

A row matches if `column_name` equals **any** of the values in the list.

### Example

```sql
SELECT
    *
FROM
    products
WHERE
    category IN ('Electronics', 'Fitness');
```

is equivalent to:

```sql
SELECT
    *
FROM
    products
WHERE
    category = 'Electronics'
    OR category = 'Fitness';
```

Result:

```bash
+----+-------------------+-------------+-------+
| id |       name        |  category   | price |
+----+-------------------+-------------+-------+
| 1  |  Wireless Mouse    | Electronics | 19.99 |
| 2  | Bluetooth Speaker  | Electronics | 45.5  |
| 3  |     Yoga Mat       |   Fitness   | 25.0  |
| 4  |   Running Shoes    |   Fitness   | 60.0  |
+----+-------------------+-------------+-------+
```

Products from the `Home` and `Office` categories are excluded, since neither category appears in the list.

---

### Exercise

Write a query that retrieves all columns from the `products` table, keeping only the rows where `category` is `'Electronics'` or `'Fitness'`.

<ul>
<li id="test-1">The result has a <code>category</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>category</code> is <code>'Electronics'</code> or <code>'Fitness'</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    products
WHERE
    category IN ('Electronics', 'Fitness');
```

</details>
