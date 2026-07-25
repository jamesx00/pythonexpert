---
lesson_name: Enforcing uniqueness with PRIMARY KEY
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1103
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1104
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1105
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

## Enforcing uniqueness with PRIMARY KEY

A `PRIMARY KEY` marks a column as the unique identifier for each row in a table. No two rows can ever share the same primary key value, and the database will reject any attempt to insert a duplicate one.

```sql
CREATE TABLE table_name (
    id PRIMARY KEY,
    column_2,
    column_3
);
```

- `id PRIMARY KEY`: Marks the `id` column as the table's primary key.

Every table you design should have a primary key. It is what lets you (and other tables, through foreign keys, which you will learn about next) reliably refer to one exact row.

---

### Exercise

Write a command that creates a table called `reviews` with the columns `id`, `product_id`, `rating`, and `comment`, where `id` is the primary key.

#### Tests

<ul>
<li id="test-1">The <code>reviews</code> table has the columns <code>id</code>, <code>product_id</code>, <code>rating</code>, and <code>comment</code>.</li>
<li id="test-2">The <code>id</code> column is set as the primary key.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
CREATE TABLE reviews (
    id PRIMARY KEY,
    product_id,
    rating,
    comment
);
```

</details>
