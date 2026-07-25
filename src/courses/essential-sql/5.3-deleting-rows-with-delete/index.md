---
lesson_name: Deleting rows with DELETE
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 806
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 807
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 808
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

## Deleting rows with DELETE

The `DELETE` statement removes rows from a table:

```sql
DELETE FROM table_name
WHERE
    condition;
```

- `table_name`: The table to delete rows from.
- `WHERE condition`: Chooses which rows get deleted.

<div class="alert-info text-sm">
<b>Never forget the WHERE clause</b><br />

Just like <code>UPDATE</code>, leaving out <code>WHERE</code> means <code>DELETE</code> removes <b>every single row</b> in the table, not just some of them. Always double check your <code>WHERE</code> clause before running a <code>DELETE</code>.

</div>

---

### Exercise

We have already created a table `orders` with the columns `id`, `customer_id`, `order_date`, `status`, and `shipped_date`. Write a command that deletes every order whose `status` is `Cancelled`, without deleting any other order.

#### Tests

<ul>
<li id="test-1">No row in <code>orders</code> has <code>status</code> equal to <code>Cancelled</code> anymore.</li>
<li id="test-2">Every order that was not <code>Cancelled</code> is still in the table.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
DELETE FROM orders
WHERE
    status = 'Cancelled';
```

</details>
