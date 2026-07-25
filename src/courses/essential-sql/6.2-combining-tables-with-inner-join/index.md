---
lesson_name: Combining tables with INNER JOIN
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 903
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 904
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 905
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

## Combining tables with INNER JOIN

In the last lesson, we joined `customers` and `orders` by writing out the full table name in front of each column, like `customers.first_name`. That works, but it gets verbose once your queries involve several tables. SQL lets us give each table a short **alias** to keep things readable.

### Table aliases

You assign an alias by writing it right after the table name (no `AS` required, though you can use it if you like):

```sql
SELECT
    oi.quantity,
    p.name
FROM
    order_items oi
INNER JOIN
    products p
ON
    oi.product_id = p.id;
```

- `order_items oi`: from now on in this query, `order_items` can be referred to as `oi`.
- `products p`: likewise, `products` can be referred to as `p`.
- `ON oi.product_id = p.id`: the join condition, written using the aliases.

Aliases don't change the result at all, they just make the query shorter and easier to read, which matters a lot once you start joining three or four tables together.

### Why the ON clause matters

Every `INNER JOIN` needs an `ON` clause that says how the two tables relate. In our database, `order_items.product_id` and `products.id` both refer to the same product, so that's what we join on:

```sql
SELECT
    oi.quantity,
    p.name,
    p.category
FROM
    order_items oi
INNER JOIN
    products p
ON
    oi.product_id = p.id;
```

Result:

```bash
+----------+-------------------+-------------+
| quantity |        name       |  category   |
+----------+-------------------+-------------+
|    3     |   Wireless Mouse  | Electronics |
|    1     | Bluetooth Speaker | Electronics |
|   .....  |       .....       |    .....    |
```

If you joined on the wrong columns (say, `oi.id = p.id`), the database wouldn't complain, it would just silently match up the wrong rows. Always double check that your `ON` condition reflects the real relationship between the tables.

---

### Exercise

Write a query that joins `order_items` (aliased `oi`) and `products` (aliased `p`) to return the product `name` and the `quantity` for every order item.

<ul>
<li id="test-1">The result has a <code>name</code> column and a <code>quantity</code> column.</li>
<li id="test-2">The result contains one row per order item, pairing the correct product <code>name</code> with the correct <code>quantity</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    p.name,
    oi.quantity
FROM
    order_items oi
INNER JOIN
    products p
ON
    oi.product_id = p.id;
```

</details>
