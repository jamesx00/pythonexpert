---
lesson_name: Creating a table with CREATE TABLE
code_editor: True
code_execution: True
adding_file_allowed: False
section: Creating and Managing Tables
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1100
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1101
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1102
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

## Creating a table with CREATE TABLE

So far we have only worked with tables that were already there for us (`customers`, `products`, `orders`, `order_items`). The `CREATE TABLE` statement is how you build a brand new table from scratch:

```sql
CREATE TABLE table_name (
    column_1,
    column_2,
    column_3
);
```

- `table_name`: The name of the new table.
- `column_1, column_2, column_3`: The names of the columns the table will have.

Every row inserted into this table will have these columns, in this order. In the next lessons you will learn how to give each column a data type and extra rules (like requiring a value, or being unique).

---

### Exercise

Write a command that creates a new table called `reviews` with the columns `id`, `product_id`, `rating`, and `comment`.

#### Tests

<ul>
<li id="test-1">A table named <code>reviews</code> exists.</li>
<li id="test-2">The <code>reviews</code> table has the columns <code>id</code>, <code>product_id</code>, <code>rating</code>, and <code>comment</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
CREATE TABLE reviews (
    id,
    product_id,
    rating,
    comment
);
```

</details>
