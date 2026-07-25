---
lesson_name: Pattern matching with LIKE
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 621
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 622
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 623
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

## Pattern matching with LIKE

`=` only matches an exact value. When you need to match part of a text value, use `LIKE` together with a wildcard.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    column_name LIKE pattern;
```

Two wildcard characters can be used inside `pattern`:

- `%` matches any sequence of zero or more characters.
- `_` matches exactly one character.

### Example

To find every customer whose first name starts with `J`, we put the `%` wildcard after it:

```sql
SELECT
    *
FROM
    customers
WHERE
    first_name LIKE 'J%';
```

Result:

```bash
+----+------------+-----------+-----+--------+
| id | first_name | last_name | age | gender |
+----+------------+-----------+-----+--------+
| 2  |  Jonathan  |   Dixon   | 71  |   F    |
| 4  |    Juan    |  Campos   | 99  |   F    |
| 10 |  Jennifer  |    Ross   | 100 |   M    |
+----+------------+-----------+-----+--------+
```

`'J%'` matches any value that starts with `J`, no matter how many characters follow. If we instead wanted names that *end* with a letter, we'd put the `%` before it, e.g. `'%n'` matches `Jonathan`. `LIKE` is case-insensitive by default in SQLite, so `'j%'` would match the same rows.

---

### Exercise

Write a query that retrieves all columns from the `customers` table, keeping only the rows where `first_name` starts with `'J'`.

<ul>
<li id="test-1">The result has a <code>first_name</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>first_name</code> starts with <code>'J'</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    customers
WHERE
    first_name LIKE 'J%';
```

</details>
