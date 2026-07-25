---
lesson_name: Combining conditions with OR
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 609
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 610
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 611
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

## Combining conditions with OR

While `AND` requires every condition to be true, `OR` only requires **at least one** of the conditions to be true.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    condition_1
    OR condition_2;
```

A row is included if `condition_1` is true, if `condition_2` is true, or if both are true.

### Example

The `orders` table has a `status` column that can be `'Pending'`, `'Shipped'`, `'Delivered'`, or `'Cancelled'`. To find every order that still needs attention, we can look for the ones that are either `'Pending'` or `'Cancelled'`:

```sql
SELECT
    *
FROM
    orders
WHERE
    status = 'Pending'
    OR status = 'Cancelled';
```

Result:

```bash
+----+-------------+------------+-----------+--------------+
| id | customer_id | order_date |  status   | shipped_date |
+----+-------------+------------+-----------+--------------+
| 1  |      3      | 2025-...   | Cancelled |     None     |
| 4  |      1      | 2025-...   | Cancelled |     None     |
| 5  |      7      | 2025-...   | Cancelled |     None     |
| .. |     ...     |    ...     |    ...    |     ...      |
```

Any order whose status is `'Shipped'` or `'Delivered'` is excluded, since it satisfies neither condition.

---

### Exercise

Write a query that retrieves all columns from the `orders` table, keeping only the rows where `status` is `'Pending'` **or** `status` is `'Cancelled'`.

<ul>
<li id="test-1">The result has a <code>status</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>status</code> is <code>'Pending'</code> or <code>'Cancelled'</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    orders
WHERE
    status = 'Pending'
    OR status = 'Cancelled';
```

</details>
