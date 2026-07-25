---
lesson_name: Filtering rows with WHERE
code_editor: True
code_execution: True
adding_file_allowed: False
section: Filtering Data
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 600
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 601
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 602
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

## Filtering rows with WHERE

So far, every query we've written returns every row in a table. The `WHERE` clause lets us keep only the rows that match a condition, filtering out the rest.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    condition;
```

`condition`: An expression that is checked for every row. Only rows where the condition is true are included in the result.

### Example

```sql
SELECT
    *
FROM
    customers;
```

returns all 10 rows. If we only want the customers whose `gender` is `'F'`, we add a `WHERE` clause:

```sql
SELECT
    *
FROM
    customers
WHERE
    gender = 'F';
```

Result:

```bash
+----+------------+-----------+-----+--------+
| id | first_name | last_name | age | gender |
+----+------------+-----------+-----+--------+
| 2  |  Jonathan  |   Dixon   | 71  |   F    |
| 4  |    Juan    |  Campos   | 99  |   F    |
| 6  |    Kyle    |   Blair   | 62  |   F    |
| 8  |   Tammy    |   Woods   | 86  |   F    |
+----+------------+-----------+-----+--------+
```

Notice that `WHERE` comes right after `FROM`, and before any `ORDER BY` or `LIMIT` clause.

---

### Exercise

Write a query that retrieves all columns from the `customers` table, keeping only the rows where `gender` is `'F'`.

<ul>
<li id="test-1">The result has a <code>gender</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>gender</code> is <code>'F'</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    customers
WHERE
    gender = 'F';
```

</details>
