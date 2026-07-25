---
lesson_name: Grouping changes with transactions
code_editor: True
code_execution: True
adding_file_allowed: False
section: Transactions and Data Integrity
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 1220
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: main.py
        file_type: python
        id: 1221
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: setup_data.py
      - file_name: tests.py
        file_type: python
        id: 1222
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

## Grouping changes with transactions

Every `INSERT`, `UPDATE`, and `DELETE` you have written so far ran on its own. But sometimes several statements only make sense as a group — for example, moving money between two bank accounts needs both the withdrawal and the deposit to happen together. If only one of them succeeded, the data would be left in a broken state.

A **transaction** groups statements together so that either all of them take effect, or none of them do:

```sql
BEGIN;

UPDATE table_name
SET
    column_name = new_value
WHERE
    condition;

COMMIT;
```

- `BEGIN`: Starts a new transaction.
- `COMMIT`: Saves every change made since `BEGIN`, permanently.
- `ROLLBACK`: Instead of `COMMIT`, this undoes every change made since `BEGIN`, as if none of it ever happened.

`ROLLBACK` is what makes transactions useful for safety: if something goes wrong partway through (or you simply change your mind), you can back out of every change at once instead of trying to manually undo each statement.

```sql
BEGIN;

UPDATE table_name
SET
    column_name = new_value
WHERE
    condition;

ROLLBACK;
```

---

### Exercise

Write a command that starts a transaction, changes the `price` of the product with `id` `1` to `999.99`, and then rolls the transaction back, so that the product's `price` ends up exactly the same as it was before.

#### Tests

<ul>
<li id="test-1">Your command uses both <code>BEGIN</code> and <code>ROLLBACK</code>.</li>
<li id="test-2">After running your command, the <code>price</code> of the product with <code>id</code> <code>1</code> is unchanged from its original value.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
BEGIN;

UPDATE products
SET
    price = 999.99
WHERE
    id = 1;

ROLLBACK;
```

</details>
