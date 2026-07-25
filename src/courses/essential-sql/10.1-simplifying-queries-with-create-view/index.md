---
lesson_name: Simplifying queries with CREATE VIEW
code_editor: True
code_execution: True
adding_file_allowed: False
section: Views
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1210
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1211
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1212
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

## Simplifying queries with CREATE VIEW

If you find yourself writing the same complex query over and over, a **view** lets you save it under a name and query it like a regular table. A view does not store any data of its own — every time you query it, the database runs the underlying query again behind the scenes.

```sql
CREATE VIEW view_name AS
SELECT
    column_1,
    column_2
FROM
    table_name
WHERE
    condition;
```

- `view_name`: The name you will use to query this view, just like a table name.
- `AS SELECT ...`: The query the view represents.

Once created, you can query the view exactly like a table:

```sql
SELECT
    *
FROM
    view_name;
```

---

### Exercise

Write a command that creates a view called `shipped_orders`, containing every column of every order from the `orders` table whose `status` is `Shipped`.

#### Tests

<ul>
<li id="test-1">A view named <code>shipped_orders</code> exists.</li>
<li id="test-2">Querying <code>shipped_orders</code> returns exactly the orders whose <code>status</code> is <code>Shipped</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
CREATE VIEW shipped_orders AS
SELECT
    *
FROM
    orders
WHERE
    status = 'Shipped';
```

</details>
