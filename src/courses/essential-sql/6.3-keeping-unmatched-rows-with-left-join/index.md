---
lesson_name: Keeping unmatched rows with LEFT JOIN
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 906
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 907
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 908
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

## Keeping unmatched rows with LEFT JOIN

`INNER JOIN` only keeps rows that have a match in **both** tables. That's a problem if you want to know about rows in one table that have **no** match in the other, for example, customers who have never placed an order.

In our sample database, every customer except one has placed at least one order. If we `INNER JOIN` `customers` with `orders`, that one customer disappears from the result entirely, because there's no matching `orders` row to pair them with.

`LEFT JOIN` fixes this. It keeps **every** row from the left table (the one listed first), whether or not it has a match on the right. When there's no match, the columns from the right table are filled in with `NULL`.

```sql
SELECT
    columns
FROM
    table_1
LEFT JOIN
    table_2
ON
    table_1.column = table_2.column;
```

- `table_1` is the "left" table: all of its rows appear in the result, matched or not.
- `table_2` is the "right" table: its columns show up as `NULL` for any `table_1` row that has no match.

### Example

```sql
SELECT
    c.first_name,
    o.status
FROM
    customers c
LEFT JOIN
    orders o
ON
    c.id = o.customer_id;
```

Result:

```bash
+------------+-----------+
| first_name |  status   |
+------------+-----------+
|   Megan    |    NULL   |
|  Jonathan  |  Shipped  |
|  Jonathan  | Delivered |
|    .....   |   .....   |
```

`Megan` (customer id 1) has never placed an order, so she still shows up once in the result, with `status` as `NULL`. Every other customer shows up once per order they've placed, just like with `INNER JOIN`.

---

### Exercise

Write a query using `LEFT JOIN` that returns every customer's `first_name`, along with the `id` of their order (aliased `order_id`), so that customers with no orders still appear in the result, with `order_id` as `NULL`.

<ul>
<li id="test-1">The result has a <code>first_name</code> column and an <code>order_id</code> column.</li>
<li id="test-2">The customer with no orders appears exactly once, with <code>order_id</code> equal to <code>NULL</code>.</li>
<li id="test-3">The total number of rows matches a <code>LEFT JOIN</code> of <code>customers</code> and <code>orders</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    c.first_name,
    o.id AS order_id
FROM
    customers c
LEFT JOIN
    orders o
ON
    c.id = o.customer_id;
```

</details>
