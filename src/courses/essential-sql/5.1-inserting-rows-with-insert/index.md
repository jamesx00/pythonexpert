---
lesson_name: Inserting rows with INSERT
code_editor: True
code_execution: True
adding_file_allowed: False
section: Modifying Data
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 800
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 801
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 802
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

## Inserting rows with INSERT

Every command we have written so far only reads data. The `INSERT` statement is how we add a brand new row to a table:

```sql
INSERT INTO table_name (column_1, column_2, column_3)
VALUES
    (value_1, value_2, value_3);
```

- `table_name`: The table to add a row to.
- `(column_1, column_2, column_3)`: The columns you are providing values for.
- `VALUES (value_1, value_2, value_3)`: The values to insert, in the same order as the column list. Text values need quotes, numbers do not.

You can insert more than one row at a time by separating each group of values with a comma:

```sql
INSERT INTO table_name (column_1, column_2)
VALUES
    (value_1, value_2),
    (value_3, value_4);
```

<div class="alert-info text-sm">
<b>Missing columns?</b><br />

If you leave a column out of the column list, it is set to <code>NULL</code> (or a default value, if the table was set up with one). You will learn how to set up default values later in this course.

</div>

---

### Exercise

We have already created a table `products` with the columns `id`, `name`, `category`, and `price`. Write a command that inserts a new product into `products`:

- `id`: `9`
- `name`: `Desk Chair`
- `category`: `Office`
- `price`: `85.00`

#### Tests

<ul>
<li id="test-1">The <code>products</code> table has exactly one more row than before.</li>
<li id="test-2">A row exists with <code>name</code> <code>Desk Chair</code>, <code>category</code> <code>Office</code>, and <code>price</code> <code>85.00</code>.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
INSERT INTO products (id, name, category, price)
VALUES
    (9, 'Desk Chair', 'Office', 85.00);
```

</details>
