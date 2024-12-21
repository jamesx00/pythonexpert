---
lesson_name: Renaming columns without AS
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 484
        is_closable: false
        is_edit_focus: false
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 485
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 486
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

## Renaming columns without AS

In the previous lesson, we changed the result column name with the keyword `AS`, but we can omit the keyword `AS` as well. For example:

```sql
SELECT
    column_1 AS new_col_1,
    column_2,
    column_3 AS new_col_3
FROM table_name;
```

can be written as

```sql
SELECT
    column_1 new_col_1,
    column_2,
    column_3 new_col_3
FROM table_name;
```

### Exercise

Write a command that retrieves the data from `customers` table and rename two columns.

- Rename column `first_name` to `name`
  {: #test-1}
- Rename column `last_name` to `lastName`
  {: #test-2}
- Must not use keyword `AS`
  {: #test-3}

Expected result

```sh
+----------+----------+
|   name   | lastName |
+----------+----------+
|  Megan   |  Chang   |
| Jonathan |  Dixon   |
|  Tammy   |  Howard  |
|   Juan   |  Campos  |
| Vanessa  |  Patel   |
|   Kyle   |  Blair   |
|  Anita   |  Gomez   |
|  Tammy   |  Woods   |
|  Bryan   | Sellers  |
| Jennifer |   Ross   |
+----------+----------+
```

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    first_name name,
    last_name lastName
FROM
    customers;
```

</details>
