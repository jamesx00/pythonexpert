---
lesson_name: Updating rows with UPDATE
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 803
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 804
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 805
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

## Updating rows with UPDATE

The `UPDATE` statement changes the values of existing rows:

```sql
UPDATE table_name
SET
    column_1 = new_value_1,
    column_2 = new_value_2
WHERE
    condition;
```

- `table_name`: The table to update.
- `SET`: Lists the columns to change and their new values.
- `WHERE condition`: Chooses which rows get updated.

<div class="alert-info text-sm">
<b>Never forget the WHERE clause</b><br />

If you leave out <code>WHERE</code>, the <code>UPDATE</code> statement changes <b>every single row</b> in the table. This is one of the most common (and most dangerous) mistakes in SQL, so always double check your <code>WHERE</code> clause before running an <code>UPDATE</code>.

</div>

---

### Exercise

We have already created a table `products` with the columns `id`, `name`, `category`, and `price`. Write a command that updates the product with `id` `7` (`Notebook`) so its `price` is `4.25`, without changing any other product.

#### Tests

<ul>
<li id="test-1">The product with <code>id</code> <code>7</code> now has a <code>price</code> of <code>4.25</code>.</li>
<li id="test-2">Every other product's <code>price</code> is unchanged.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
UPDATE products
SET
    price = 4.25
WHERE
    id = 7;
```

</details>
