---
lesson_name: Removing a table with DROP TABLE
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1112
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1113
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1114
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

## Removing a table with DROP TABLE

The `DROP TABLE` statement permanently removes a table and every row it contains:

```sql
DROP TABLE table_name;
```

- `table_name`: The table to remove.

<div class="alert-info text-sm">
<b>There is no undo</b><br />

Unlike <code>DELETE</code>, which removes rows but keeps the table itself, <code>DROP TABLE</code> removes the table's structure and all of its data at once. There is no <code>WHERE</code> clause to narrow it down — always be certain before running it.

</div>

---

### Exercise

Write a command that removes the `order_items` table entirely, without affecting any other table.

#### Tests

<ul>
<li id="test-1">The <code>order_items</code> table no longer exists.</li>
<li id="test-2">The <code>customers</code>, <code>products</code>, and <code>orders</code> tables still exist.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
DROP TABLE order_items;
```

</details>
