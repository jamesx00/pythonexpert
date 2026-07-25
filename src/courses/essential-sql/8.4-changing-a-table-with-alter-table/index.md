---
lesson_name: Changing a table with ALTER TABLE
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1109
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1110
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1111
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

## Changing a table with ALTER TABLE

Once a table already has data in it, you can't just recreate it from scratch to change its structure. The `ALTER TABLE` statement lets you modify an existing table in place. The most common use is adding a new column:

```sql
ALTER TABLE table_name
ADD COLUMN column_name;
```

- `table_name`: The table to change.
- `ADD COLUMN column_name`: Adds a new column to every row of the table. Existing rows get `NULL` for the new column, since there is no value for it yet.

---

### Exercise

Write a command that adds a new column called `email` to the `customers` table, without changing any of the existing rows.

#### Tests

<ul>
<li id="test-1">The <code>customers</code> table now has an <code>email</code> column.</li>
<li id="test-2">The <code>customers</code> table still has the same number of rows as before.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
ALTER TABLE customers
ADD COLUMN email;
```

</details>
