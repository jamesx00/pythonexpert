---
lesson_name: Summing values with SUM
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 703
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 704
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 705
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

## Summing values with SUM

`SUM` is another aggregate function. Instead of counting rows, it adds up the values in a numeric column across all the rows.

```sql
SELECT
    SUM(column_name) AS total
FROM
    table_name;
```

`SUM(column_name)` adds together every value in `column_name`. Rows where the column is `NULL` are ignored rather than treated as zero.

### Example

```sql
SELECT
    SUM(age) AS total_age
FROM
    customers;
```

Result:

```bash
+-----------+
| total_age |
+-----------+
|    716    |
+-----------+
```

This adds up the `age` column across every row in `customers` into a single number.

---

### Exercise

The `order_items` table has one row per product in an order, with a `quantity` column showing how many units were bought. Write a command that sums up the `quantity` column across every row in `order_items`.

<ul>
<li id="test-1">The result has a <code>total_quantity</code> column.</li>
<li id="test-2">The value of <code>total_quantity</code> matches the sum of the <code>quantity</code> column in <code>order_items</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    SUM(quantity) AS total_quantity
FROM
    order_items;
```

</details>
