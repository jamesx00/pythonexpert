---
lesson_name: Renaming columns with AS
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 477
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 478
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 479
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

## Renaming columns with AS

In SQL, the `AS` keyword is used to rename a column or a table with an alias in the result set of a query. Renaming columns can improve the readability of the output, provide meaningful names, or alias calculations.

### Syntax

The basic syntax for renaming columns with `AS` is as follows:

```sql
SELECT column_name AS new_name
FROM table_name;
```

`column_name`: The original name of the column you want to rename.

`new_name`: The desired new name for the column.

`table_name`: The name of the table from which to retrieve the data.

We could rename multiple columns with below syntax:

```sql
SELECT
    column_1 AS new_col_1,
    column_2,
    column_3 AS new_col_3
FROM table_name;
```

In the above example, we rename `column_1` to `new_col_1` and `column_3` to `new_col_3` while keeping the `column_2` the same. _Notice that we can write the command in multiple lines instead of a single line for readability._

### Example

Here's our regular `SELECT` command:

```sql
SELECT first_name, last_name
FROM customers;
```

Result:

```bash
+------------+-----------+
| first_name | last_name |
+------------+-----------+
|   Megan    |   Chang   |
|   .....    |   .....   |
```

We can rename any of the columns with `AS` keyword. For example, this command:

```sql
SELECT first_name AS name, last_name
FROM customers;
```

will get you below result:

```bash
+----------+-----------+
|   name   | last_name |
+----------+-----------+
|  Megan   |   Chang   |
|  .....   |   .....   |
```

---

### Exercise

Write a command that retrieves the data from `customers` table and rename two columns.

<ul>
<li id="test-1">Rename column <code>first_name</code> to <code>name</code>.</li>
<li id="test-2">Rename column <code>last_name</code> to <code>lastName</code>.</li>
</ul>

Expected result

```sh
+----------+----------+
|   name   | lastName |
+----------+----------+
|  Megan   |  Chang   |
| Jonathan |  Dixon   |
|  Tammy   |  Howard  |
|   Juan   |  Campos  |
| Vanessa  |  Patel   |
|   Kyle   |  Blair   |
|  Anita   |  Gomez   |
|  Tammy   |  Woods   |
|  Bryan   | Sellers  |
| Jennifer |   Ross   |
+----------+----------+
```

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT
    first_name AS name,
    last_name AS lastName
FROM
    customers;
```

</details>
