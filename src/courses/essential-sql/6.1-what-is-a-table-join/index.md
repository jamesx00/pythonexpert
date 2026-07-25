---
lesson_name: What is a table join
code_editor: True
code_execution: True
adding_file_allowed: False
section: Joining Tables
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 900
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 901
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 902
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

## What is a table join

So far, every query we've written has looked at a single table. In a real database, data is usually spread across several tables. For example, in our sample database:

- The `customers` table holds each customer's `first_name`, `last_name`, `age`, and `gender`.
- The `orders` table holds each order's `id`, `customer_id`, `order_date`, and `status`.

Notice that the `orders` table doesn't store the customer's name, only a `customer_id`. If we want to see the customer's name next to their order status, we need to combine, or **join**, rows from both tables.

A **join** combines rows from two tables based on a related column between them. Here, `customers.id` and `orders.customer_id` refer to the same customer, so we can use them to match up the rows.

### INNER JOIN syntax

The most common type of join is `INNER JOIN`:

```sql
SELECT
    columns
FROM
    table_1
INNER JOIN
    table_2
ON
    table_1.column = table_2.column;
```

- `INNER JOIN table_2`: the table we want to combine with `table_1`.
- `ON table_1.column = table_2.column`: tells the database **how** the two tables relate to each other. Without an `ON` condition, the database wouldn't know which row in `table_1` belongs with which row in `table_2`.

### Example

```sql
SELECT
    customers.first_name,
    orders.status
FROM
    customers
INNER JOIN
    orders
ON
    customers.id = orders.customer_id;
```

Result:

```bash
+------------+-----------+
| first_name |  status   |
+------------+-----------+
|  Jonathan  |  Shipped  |
|   Tammy    | Delivered |
|    .....   |   .....   |
```

Each row in the result pairs a customer's `first_name` with the `status` of one of their orders. If a customer placed 3 orders, they will show up 3 times in the result, once per order. Notice we wrote `customers.first_name` and `orders.status` instead of just `first_name` and `status` — this is called **qualifying** a column name with its table. It's required whenever the column name could be ambiguous (for example, both tables might have an `id` column), and it's good practice any time you're joining tables, even if the column names don't clash.

---

### Exercise

Write a query that joins `customers` and `orders` on `customers.id = orders.customer_id`, returning the customer's `first_name` and the order's `status` for every order.

<ul>
<li id="test-1">The result has a <code>first_name</code> column and a <code>status</code> column.</li>
<li id="test-2">The result contains one row for every order, pairing the correct <code>first_name</code> with the correct <code>status</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    customers.first_name,
    orders.status
FROM
    customers
INNER JOIN
    orders
ON
    customers.id = orders.customer_id;
```

</details>
