---
lesson_name: Filtering a range with BETWEEN
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 615
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 616
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 617
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

## Filtering a range with BETWEEN

Checking a range with `>=` and `<=` combined by `AND` works, but SQL gives us a shorter way to write it: `BETWEEN`.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    column_name BETWEEN low_value AND high_value;
```

`BETWEEN` keeps rows where the value is greater than or equal to `low_value` **and** less than or equal to `high_value`. Both endpoints are included.

### Example

```sql
SELECT
    *
FROM
    products
WHERE
    price BETWEEN 20 AND 50;
```

is equivalent to:

```sql
SELECT
    *
FROM
    products
WHERE
    price >= 20
    AND price <= 50;
```

Result:

```bash
+----+-------------------+-------------+-------+
| id |       name        |  category   | price |
+----+-------------------+-------------+-------+
| 2  | Bluetooth Speaker  | Electronics | 45.5  |
| 3  |     Yoga Mat       |   Fitness   | 25.0  |
| 6  |    Desk Lamp       |    Home     | 22.0  |
| 8  |      Backpack      |   Office    | 40.0  |
+----+-------------------+-------------+-------+
```

Products priced below `20` or above `50`, like the `Wireless Mouse` and the `Running Shoes`, are excluded.

---

### Exercise

Write a query that retrieves all columns from the `products` table, keeping only the rows where `price` is between `20` and `50`, inclusive.

<ul>
<li id="test-1">The result has a <code>price</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>price</code> is between <code>20</code> and <code>50</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    products
WHERE
    price BETWEEN 20 AND 50;
```

</details>
