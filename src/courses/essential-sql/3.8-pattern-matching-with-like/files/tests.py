import sqlite3
import main
import sys
import json

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

def get_column(table, columns, col_name):
    idx = -1 if col_name not in columns else columns.index(col_name)
    if idx == -1:
        return None
    return [row[idx] for row in table]

try:
    query = open('query.sql', 'r').read()
    cur.execute(query)
    result_columns = [] if cur.description is None else [c[0] for c in cur.description]
    result_table = cur.fetchall()

    cur.execute("SELECT * FROM customers WHERE first_name LIKE 'J%';")
    expected_columns = [c[0] for c in cur.description]
    expected_table = cur.fetchall()

    results = {}

    name_values = get_column(result_table, result_columns, "first_name")
    results[1] = name_values is not None

    result_ids = get_column(result_table, result_columns, "id")
    expected_ids = get_column(expected_table, expected_columns, "id")
    results[2] = result_ids is not None and sorted(result_ids) == sorted(expected_ids)

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
