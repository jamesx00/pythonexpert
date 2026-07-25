---
lesson_name: Filtering groups with HAVING
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 715
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 716
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 717
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

## Filtering groups with HAVING

`WHERE` filters individual rows *before* they are grouped, so it can't refer to an aggregate function like `COUNT(*)`. To filter groups *after* they've been aggregated, for example, "only show categories with more than 5 products", you need `HAVING`.

```sql
SELECT column_name, AGGREGATE_FUNCTION(other_column) AS agg
FROM table_name
GROUP BY column_name
HAVING AGGREGATE_FUNCTION(other_column) > value;
```

`HAVING` works just like `WHERE`, except its condition is checked against the aggregated value of each group instead of each raw row, and it always comes after `GROUP BY`.

### Example

```sql
SELECT status, COUNT(*) AS total
FROM orders
GROUP BY status
HAVING COUNT(*) > 5;
```

Result:

```bash
+-----------+-------+
|  status   | total |
+-----------+-------+
| Cancelled |   8   |
|  Shipped  |   7   |
+-----------+-------+
```

Here, `orders` is grouped by `status`, and only the groups with more than 5 orders are kept, `Delivered` and `Pending` had 5 or fewer orders so they are dropped entirely.

---

### Exercise

Write a command that groups the `orders` table by `customer_id`, counting how many orders each customer has, and keeps only the customers with **more than 2** orders.

<ul>
<li id="test-1">The result has a <code>customer_id</code> column and a <code>total</code> column.</li>
<li id="test-2">Only customers with more than 2 orders appear, each with the correct order count.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT customer_id, COUNT(*) AS total
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 2;
```

</details>
