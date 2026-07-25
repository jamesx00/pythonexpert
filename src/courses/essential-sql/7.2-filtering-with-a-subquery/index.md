---
lesson_name: Filtering with a subquery
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1003
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1004
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1005
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

## Filtering with a subquery

In the previous lesson, we used a subquery that returned a single value. But a subquery can also return a list of values. When that's the case, we can't use `=` or `>` to compare against it — instead, we use `IN`, which checks whether a value exists anywhere in that list.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    column_name IN (
        SELECT other_column
        FROM other_table
    );
```

The inner query runs first and produces a list of values. The outer query then keeps only the rows where `column_name` matches one of those values.

### Example

Suppose we want to find every product that has been ordered at least once. The `order_items` table records which `product_id` was included in each order, so we can pull the list of ordered product ids with a subquery:

```sql
SELECT
    name
FROM
    products
WHERE
    id IN (
        SELECT product_id
        FROM order_items
    );
```

The subquery `SELECT product_id FROM order_items` returns a list of product ids (with duplicates, since a product can be ordered many times). `IN` doesn't care about duplicates or order — it simply checks whether each product's `id` appears anywhere in that list.

---

### Exercise

Write a command that retrieves the `first_name` of every customer who has placed at least one order. Use a subquery on the `orders` table with `IN` to find which `id` values from `customers` have a matching order.

<ul>
<li id="test-1">The result has a <code>first_name</code> column.</li>
<li id="test-2">The result contains the first names of exactly the customers who have placed at least one order (no more, no fewer).</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    first_name
FROM
    customers
WHERE
    id IN (
        SELECT customer_id
        FROM orders
    );
```

</details>
