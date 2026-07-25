---
lesson_name: Speeding up queries with CREATE INDEX
code_editor: True
code_execution: True
adding_file_allowed: False
section: Indexing
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1200
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1201
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1202
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

## Speeding up queries with CREATE INDEX

Without any help, the database has to check every single row of a table to find the ones matching a `WHERE` condition. On a small table like `orders` that is instant, but on a table with millions of rows it can be slow. An **index** solves this by keeping a separate, pre-sorted lookup structure for a column, so the database can jump straight to the matching rows instead of scanning the whole table.

```sql
CREATE INDEX index_name
ON table_name (column_name);
```

- `index_name`: A name for the new index.
- `table_name (column_name)`: The table and column the index is built on.

An index speeds up `WHERE`, `ORDER BY`, and `JOIN` operations that use the indexed column, at the cost of a small amount of extra storage and slightly slower `INSERT`/`UPDATE`/`DELETE` operations on that column (since the index has to be kept up to date too).

---

### Exercise

Write a command that creates an index on the `customer_id` column of the `orders` table.

#### Tests

<ul>
<li id="test-1">An index exists on the <code>customer_id</code> column of the <code>orders</code> table.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
CREATE INDEX idx_orders_customer_id
ON orders (customer_id);
```

</details>
