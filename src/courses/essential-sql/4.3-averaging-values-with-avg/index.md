---
lesson_name: Averaging values with AVG
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 706
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 707
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 708
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

## Averaging values with AVG

`AVG` is an aggregate function that computes the mean of a numeric column across all the rows.

```sql
SELECT
    AVG(column_name) AS average
FROM
    table_name;
```

`AVG(column_name)` adds up every value in `column_name` and divides by the number of rows. Like `SUM`, rows where the column is `NULL` are skipped rather than counted as zero.

### Example

```sql
SELECT
    AVG(age) AS average_age
FROM
    customers;
```

Result:

```bash
+--------------+
| average_age  |
+--------------+
|    71.6      |
+--------------+
```

This tells us the mean `age` across all rows in `customers`.

---

### Exercise

Write a command that computes the average `price` across every row in the `products` table.

<ul>
<li id="test-1">The result has an <code>average_price</code> column.</li>
<li id="test-2">The value of <code>average_price</code> matches the average of the <code>price</code> column in <code>products</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    AVG(price) AS average_price
FROM
    products;
```

</details>
