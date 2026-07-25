---
lesson_name: Subqueries in the FROM clause
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1006
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1007
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1008
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

## Subqueries in the FROM clause

So far we've used subqueries inside `WHERE`. A subquery can also appear in the `FROM` clause. When it does, it acts as a temporary table — often called a "derived table" — that only exists for the duration of the outer query, and that you can `SELECT` from just like a regular table.

### Syntax

```sql
SELECT
    column_name
FROM
    (
        SELECT ...
        FROM table_name
    ) AS alias_name;
```

The inner query runs first and produces a result set. That result set is then treated as if it were a table named `alias_name`, and the outer query runs against it. Just like a real table, a derived table must be given an alias with `AS` so the outer query has a name to refer to it by.

### Example

Suppose we already know how to count orders per customer:

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM
    orders
GROUP BY
    customer_id;
```

This gives us one row per customer, with their order count. Now, if we want to find the largest number of orders placed by any single customer, we can wrap that query in parentheses, alias it, and query it further:

```sql
SELECT
    MAX(order_count) AS max_orders
FROM
    (
        SELECT
            customer_id,
            COUNT(*) AS order_count
        FROM
            orders
        GROUP BY
            customer_id
    ) AS customer_order_counts;
```

The inner query produces a derived table called `customer_order_counts` with columns `customer_id` and `order_count`. The outer query then simply selects the maximum `order_count` from it.

---

### Exercise

Write a command that computes the average number of orders per customer. Do this by first building a derived table in the `FROM` clause that counts orders grouped by `customer_id`, then taking the average of that count in the outer query. Alias the result column as `avg_orders`.

<ul>
<li id="test-1">The result has an <code>avg_orders</code> column.</li>
<li id="test-2">The value of <code>avg_orders</code> matches the average number of orders per customer.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    AVG(order_count) AS avg_orders
FROM
    (
        SELECT
            customer_id,
            COUNT(*) AS order_count
        FROM
            orders
        GROUP BY
            customer_id
    ) AS customer_order_counts;
```

</details>
