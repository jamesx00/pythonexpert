---
lesson_name: Negating conditions with NOT
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 612
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 613
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 614
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

## Negating conditions with NOT

The `NOT` keyword flips a condition: rows that used to match are excluded, and rows that used to fail now match.

### Syntax

```sql
SELECT
    column_name
FROM
    table_name
WHERE
    NOT condition;
```

### Example

Instead of listing every category we do want, we can ask for every product that is **not** in the `'Office'` category:

```sql
SELECT
    *
FROM
    products
WHERE
    NOT category = 'Office';
```

Result:

```bash
+----+-------------------+-------------+-------+
| id |       name        |  category   | price |
+----+-------------------+-------------+-------+
| 1  |  Wireless Mouse    | Electronics | 19.99 |
| 2  | Bluetooth Speaker  | Electronics | 45.5  |
| 3  |     Yoga Mat       |   Fitness   | 25.0  |
| 4  |   Running Shoes    |   Fitness   | 60.0  |
| 5  |    Coffee Mug      |    Home     |  8.5  |
| 6  |    Desk Lamp       |    Home     | 22.0  |
+----+-------------------+-------------+-------+
```

`Notebook` and `Backpack`, the two `'Office'` products, are left out. `NOT` can be placed in front of any condition, including ones that use `AND`, `OR`, or the operators from earlier lessons.

---

### Exercise

Write a query that retrieves all columns from the `products` table, keeping only the rows where `category` is **not** `'Office'`.

<ul>
<li id="test-1">The result has a <code>category</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>category</code> is not <code>'Office'</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    products
WHERE
    NOT category = 'Office';
```

</details>
