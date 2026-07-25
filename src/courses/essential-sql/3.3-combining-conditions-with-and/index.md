---
lesson_name: Combining conditions with AND
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 606
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 607
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 608
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

## Combining conditions with AND

Sometimes one condition isn't enough. The `AND` keyword lets you combine multiple conditions in a `WHERE` clause, keeping only the rows where **all** of them are true.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    condition_1
    AND condition_2;
```

A row is only included if `condition_1` **and** `condition_2` are both true.

### Example

```sql
SELECT
    *
FROM
    customers
WHERE
    gender = 'F'
    AND age > 65;
```

Result:

```bash
+----+------------+-----------+-----+--------+
| id | first_name | last_name | age | gender |
+----+------------+-----------+-----+--------+
| 2  |  Jonathan  |   Dixon   | 71  |   F    |
| 4  |    Juan    |  Campos   | 99  |   F    |
| 8  |   Tammy    |   Woods   | 86  |   F    |
+----+------------+-----------+-----+--------+
```

Kyle, who is `'F'` but only `62` years old, is filtered out because she fails the second condition. You can chain more than two conditions by adding more `AND` keywords.

---

### Exercise

Write a query that retrieves all columns from the `customers` table, keeping only the rows where `gender` is `'F'` **and** `age` is greater than `65`.

<ul>
<li id="test-1">The result has an <code>age</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>gender</code> is <code>'F'</code> and <code>age</code> is greater than <code>65</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    customers
WHERE
    gender = 'F'
    AND age > 65;
```

</details>
