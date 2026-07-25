---
lesson_name: Grouping rows with GROUP BY
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 712
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 713
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 714
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

## Grouping rows with GROUP BY

The aggregate functions we've seen so far (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) collapse an entire table into a single row. But often you want a separate summary for each distinct value in a column, for example, "how many products are in each category?" That's what `GROUP BY` is for.

```sql
SELECT column_name, AGGREGATE_FUNCTION(other_column)
FROM table_name
GROUP BY column_name;
```

`GROUP BY column_name` splits the rows into buckets, one per distinct value of `column_name`, and the aggregate function is then computed separately within each bucket instead of across the whole table.

### Example

```sql
SELECT
    gender,
    COUNT(*) AS total
FROM
    customers
GROUP BY
    gender;
```

Result:

```bash
+--------+-------+
| gender | total |
+--------+-------+
|   F    |   4   |
|   M    |   6   |
+--------+-------+
```

Instead of one count for the whole table, we get one count per distinct `gender` value.

---

### Exercise

Write a command that, for each `category` in the `products` table, counts how many products belong to it.

<ul>
<li id="test-1">The result has a <code>category</code> column and a <code>total</code> column.</li>
<li id="test-2">Each <code>category</code> shows the correct count of products in that category.</li>
</ul>

_Note: in this particular dataset every category happens to have exactly 2 products, so the counts will look uniform here. In a real dataset, different categories would usually have different counts._

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT category, COUNT(*) AS total
FROM products
GROUP BY category;
```

</details>
