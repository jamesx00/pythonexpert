---
lesson_name: What is a subquery
code_editor: True
code_execution: True
adding_file_allowed: False
section: Subqueries
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1000
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1001
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1002
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

## What is a subquery

A subquery is a `SELECT` statement nested inside another SQL statement. It runs first, and its result is used by the outer (main) query. Subqueries are often used in places where a single value or a list of values is expected, such as inside a `WHERE` clause.

### Syntax

A subquery is simply wrapped in parentheses:

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    column_name > (
        SELECT AVG(column_name)
        FROM table_name
    );
```

Here, `(SELECT AVG(column_name) FROM table_name)` is the subquery. Since it returns a single value (the average), it can be compared directly with `>`, just like a regular number.

### Example

Suppose we want to find products that cost more than the cheapest product. We first need to know the minimum price, then compare each product's price against it:

```sql
SELECT
    name
FROM
    products
WHERE
    price > (
        SELECT MIN(price)
        FROM products
    );
```

The database first runs the inner query `SELECT MIN(price) FROM products`, which returns a single number. That number is then substituted into the outer query, so it behaves as if we had written `WHERE price > 3.50`.

<div class="alert-info text-sm">
<b>One value only</b><br />

When a subquery is used with a comparison operator like <code>=</code>, <code>&gt;</code>, or <code>&lt;</code>, it must return exactly one row and one column. If it returns more than one row, the database will raise an error.

</div>

---

### Exercise

Write a command that retrieves the `name` of every product from the `products` table whose `price` is greater than the average price of all products. Use a subquery to calculate the average price instead of a hardcoded number.

<ul>
<li id="test-1">The result has a <code>name</code> column.</li>
<li id="test-2">The result contains the names of exactly the products priced above the average price of all products.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    name
FROM
    products
WHERE
    price > (
        SELECT AVG(price)
        FROM products
    );
```

</details>
