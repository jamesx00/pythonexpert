---
lesson_name: Counting rows with COUNT
code_editor: True
code_execution: True
adding_file_allowed: False
section: Aggregating Data
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 700
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 701
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 702
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

## Counting rows with COUNT

So far we've only pulled raw rows out of a table. Sometimes you don't want the rows themselves, you want a summary of them, for example, "how many rows are there?" That's what aggregate functions are for: they take many rows and collapse them into a single value. `COUNT` is the simplest one, it counts rows.

```sql
SELECT
    COUNT(*)
FROM
    table_name;
```

`COUNT(*)` counts every row in the table, regardless of whether any column is `NULL`. As with any column, you can give the result a friendlier name with `AS`:

```sql
SELECT
    COUNT(*) AS total
FROM
    table_name;
```

### Example

```sql
SELECT
    COUNT(*) AS total
FROM
    customers;
```

Result:

```bash
+-------+
| total |
+-------+
|  10   |
+-------+
```

This tells us there are 10 rows in the `customers` table, without us having to fetch and count them ourselves.

---

### Exercise

Write a command that counts the total number of rows in the `products` table.

<ul>
<li id="test-1">The result has a <code>total</code> column.</li>
<li id="test-2">The value of <code>total</code> matches the number of rows in <code>products</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    COUNT(*) AS total
FROM
    products;
```

</details>
