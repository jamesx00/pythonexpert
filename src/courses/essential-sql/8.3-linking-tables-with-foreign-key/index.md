---
lesson_name: Linking tables with FOREIGN KEY
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1106
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1107
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1108
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

## Linking tables with FOREIGN KEY

You already used columns like `customer_id` and `product_id` to join tables together in the joins section. A `FOREIGN KEY` makes that relationship official: it tells the database that a column's values must match a primary key value in another table.

```sql
CREATE TABLE table_name (
    id PRIMARY KEY,
    other_table_id REFERENCES other_table(id)
);
```

- `other_table_id REFERENCES other_table(id)`: Declares that `other_table_id` refers to the `id` column of `other_table`.

This is exactly the same relationship that already exists between `order_items.product_id` and `products.id`, or between `orders.customer_id` and `customers.id` — a foreign key just makes it explicit in the table definition, so the database (and anyone reading the schema) knows the two tables are linked.

---

### Exercise

Write a command that creates a table called `reviews` with the columns `id` (as the primary key), `product_id`, `rating`, and `comment`, where `product_id` references the `id` column of the `products` table.

#### Tests

<ul>
<li id="test-1">The <code>reviews</code> table has a foreign key on <code>product_id</code> that references <code>products(id)</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
CREATE TABLE reviews (
    id PRIMARY KEY,
    product_id REFERENCES products(id),
    rating,
    comment
);
```

</details>
