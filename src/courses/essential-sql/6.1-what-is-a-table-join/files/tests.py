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

    results = {}

    name_index = -1 if "first_name" not in result_columns else result_columns.index("first_name")
    status_index = -1 if "status" not in result_columns else result_columns.index("status")

    results[1] = name_index != -1 and status_index != -1

    if results[1]:
        result_rows = sorted((row[name_index], row[status_index]) for row in result_table)

        cur.execute(
            "SELECT customers.first_name, orders.status "
            "FROM customers "
            "INNER JOIN orders ON customers.id = orders.customer_id;"
        )
        expected_rows = sorted((row[0], row[1]) for row in cur.fetchall())

        results[2] = result_rows == expected_rows
    else:
        results[2] = False

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
