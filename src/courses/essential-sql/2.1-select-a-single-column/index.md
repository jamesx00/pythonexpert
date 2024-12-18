---
lesson_name: Select a single column
code_editor: True
code_execution: True
adding_file_allowed: False
section: Basic Data Retrieval
file_groups:
  - common: false
    files:
      - file_name: query.sql
        file_type: sql
        id: 470
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: query.sql
      - file_name: tests.py
        file_type: python
        id: 472
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 471
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: true
        is_test_file: false
        source: main.py
    id: 1
    name: Python
---

## Select a single column

### What are SQL statements

SQL statements are commands used to perform operations on a relational database. These statements are essential for interacting with the database, whether it's for querying data, updating records, or managing the structure of the database.

### SELECT command

The `SELECT` command in SQL is used to retrieve data from one or more tables in a relational database. It allows users to specify the columns they want to retrieve, the table or tables from which to retrieve the data, and conditions to filter the results. The `SELECT` statement is a fundamental component of SQL queries and is extensively used for data retrieval and analysis.

The basic syntax of the `SELECT` statement is as follows:

```sql
SELECT column_name FROM table;
```

- `column_name`: Specify the column you want to retrieve.
- `table`: Specifies the table from which to retrieve the data.

<div class="alert-info text-sm">
<b>Semicolon after SQL Statements?</b><br />

Semicolon is the standard way to separate each SQL statement in database systems that allows more than one SQL statement to be executed in a single call.

Some database systems require a semicolon `;` at the end of each SQL statement.

In this course, we will use semicolon at the end of each SQL statement for clarity.

</div>

---

### Exercise

We have already created a table `customers` with the columns `first_name`, `last_name`, `age`, and `gender`. Write a command to retrieve `first_name` column from `customers` table.

#### Tests

<ul>
<li id="test-1">The result has <code>first_name</code> column.</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```sql
SELECT first_name FROM customers;
```

</details>
