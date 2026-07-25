---
lesson_name: Joining three tables
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 909
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 910
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 911
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

## Joining three tables

Joins aren't limited to two tables, you can chain as many `JOIN` clauses as you need, one after another. This is common when the information you want is spread across more than two related tables.

In our database, `orders` and `products` aren't directly connected, there's no `product_id` column on `orders`. Instead, they're connected through `order_items`, which has both an `order_id` and a `product_id`. To get from `orders` to `products`, we need to join through `order_items` in the middle.

```sql
SELECT
    columns
FROM
    table_1
INNER JOIN
    table_2
ON
    table_1.column = table_2.column
INNER JOIN
    table_3
ON
    table_2.column = table_3.column;
```

Each `INNER JOIN ... ON` pair adds one more table to the result, matched using whatever column connects it to a table already in the query.

### Example

```sql
SELECT
    o.id AS order_id,
    o.status,
    p.name
FROM
    orders o
INNER JOIN
    order_items oi
ON
    o.id = oi.order_id
INNER JOIN
    products p
ON
    oi.product_id = p.id;
```

Result:

```bash
+----------+-----------+-------------------+
| order_id |  status   |        name       |
+----------+-----------+-------------------+
|    1     | Delivered |   Wireless Mouse  |
|    1     | Delivered | Bluetooth Speaker |
|    2     |  Shipped  |      Yoga Mat     |
|   .....  |   .....   |       .....       |
```

We first join `orders` to `order_items` on `o.id = oi.order_id`, then join the result to `products` on `oi.product_id = p.id`. The order of the joins matters for readability, but as long as each `ON` condition correctly links two tables that are already available, the result is the same.

---

### Exercise

Write a query joining `orders`, `order_items`, and `products` to return, for every order item, the order's `id` (aliased `order_id`), the product's `name`, and the `quantity`.

<ul>
<li id="test-1">The result has an <code>order_id</code> column, a <code>name</code> column, and a <code>quantity</code> column.</li>
<li id="test-2">The result contains one row per order item, with the correct <code>order_id</code>, product <code>name</code>, and <code>quantity</code> in each row.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    o.id AS order_id,
    p.name,
    oi.quantity
FROM
    orders o
INNER JOIN
    order_items oi
ON
    o.id = oi.order_id
INNER JOIN
    products p
ON
    oi.product_id = p.id;
```

</details>
