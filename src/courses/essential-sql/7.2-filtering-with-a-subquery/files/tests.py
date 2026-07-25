import sqlite3
import main
import sys
import json

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

try:
    query = open('query.sql', 'r').read()
    cur.execute(query)
    result_columns = [] if cur.description is None else [c[0] for c in cur.description]
    result_table = cur.fetchall()

    name_index = -1 if "first_name" not in result_columns else result_columns.index("first_name")
    result_names = set(row[name_index] for row in result_table) if name_index != -1 else set()

    cur.execute("SELECT first_name FROM customers WHERE id IN (SELECT customer_id FROM orders);")
    expected_names = set(row[0] for row in cur.fetchall())

    results = {}

    results[1] = name_index != -1
    results[2] = name_index != -1 and result_names == expected_names

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
