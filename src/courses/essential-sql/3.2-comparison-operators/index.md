---
lesson_name: Comparison operators
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 603
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 604
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 605
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

## Comparison operators

The condition in a `WHERE` clause is usually built with a comparison operator. SQL supports the following:

| Operator | Meaning |
| --- | --- |
| `=` | equal to |
| `<>` or `!=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

### Example

```sql
SELECT
    *
FROM
    products
WHERE
    price > 30;
```

Result:

```bash
+----+-------------------+-------------+-------+
| id |       name        |  category   | price |
+----+-------------------+-------------+-------+
| 2  | Bluetooth Speaker  | Electronics | 45.5  |
| 4  |   Running Shoes    |   Fitness   |  60.0 |
| 8  |      Backpack      |   Office    |  40.0 |
+----+-------------------+-------------+-------+
```

Only the products with a `price` greater than `30` are kept. You can use any of the comparison operators above the same way, for example:

```sql
SELECT
    *
FROM
    products
WHERE
    category <> 'Office';
```

keeps every row whose `category` is not `'Office'`.

---

### Exercise

Write a query that retrieves all columns from the `products` table, keeping only the rows where `price` is greater than `30`.

<ul>
<li id="test-1">The result has a <code>price</code> column.</li>
<li id="test-2">The result contains exactly the rows where <code>price</code> is greater than <code>30</code>, and no others.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    *
FROM
    products
WHERE
    price > 30;
```

</details>
