---
lesson_name: Checking for NULL values
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 624
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 625
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 626
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

## Checking for NULL values

`NULL` represents a missing or unknown value. It isn't equal to anything, not even to another `NULL`, so `= NULL` never matches. To check for it, SQL gives us the dedicated `IS NULL` (and `IS NOT NULL`) operators.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    column_name IS NULL;
```

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    column_name IS NOT NULL;
```

### Example

In the `orders` table, `shipped_date` is `NULL` whenever an order hasn't shipped yet, that is, when its `status` is `'Pending'` or `'Cancelled'`. We can find those orders directly:

```sql
SELECT
    *
FROM
    orders
WHERE
    shipped_date IS NULL;
```

Result:

```bash
+----+-------------+------------+-----------+--------------+
| id | customer_id | order_date |  status   | shipped_date |
+----+-------------+------------+-----------+--------------+
| 1  |      3      | 2025-...   | Cancelled |     None     |
| 4  |      1      | 2025-...   | Cancelled |     None     |
| 17 |      9      | 2025-...   |  Pending  |     None     |
| .. |     ...     |    ...     |    ...    |     ...      |
```

If we wanted the opposite, the orders that *have* shipped, we would use `WHERE shipped_date IS NOT NULL` instead.

---

### Exercise

Write a query that retrieves all columns from the `orders` table, keeping only the rows where `shipped_date` is `NULL`.

<ul>
<li id="test-1">The result has a <code>shipped_date</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>shipped_date</code> is <code>NULL</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    orders
WHERE
    shipped_date IS NULL;
```

</details>
