---
lesson_name: Finding extremes with MIN and MAX
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 709
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 710
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 711
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

## Finding extremes with MIN and MAX

`MIN` and `MAX` are aggregate functions that find the smallest and largest value in a column. You can use them together in the same query, since a query can compute more than one aggregate at once.

```sql
SELECT
    MIN(column_name) AS smallest,
    MAX(column_name) AS largest
FROM
    table_name;
```

### Example

```sql
SELECT
    MIN(age) AS youngest,
    MAX(age) AS oldest
FROM
    customers;
```

Result:

```bash
+----------+--------+
| youngest | oldest |
+----------+--------+
|    21    |  100   |
+----------+--------+
```

This gives us the smallest and the largest `age` in `customers`, both in a single query.

---

### Exercise

Write a single command that finds the cheapest and the most expensive product in the `products` table.

<ul>
<li id="test-1">The result has a <code>min_price</code> column matching the smallest <code>price</code> in <code>products</code>.</li>
<li id="test-2">The result has a <code>max_price</code> column matching the largest <code>price</code> in <code>products</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM
    products;
```

</details>
