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

    name_index = -1 if "name" not in result_columns else result_columns.index("name")
    qty_index = -1 if "quantity" not in result_columns else result_columns.index("quantity")

    results[1] = name_index != -1 and qty_index != -1

    if results[1]:
        result_rows = sorted((row[name_index], row[qty_index]) for row in result_table)

        cur.execute(
            "SELECT p.name, oi.quantity "
            "FROM order_items oi "
            "INNER JOIN products p ON oi.product_id = p.id;"
        )
        expected_rows = sorted((row[0], row[1]) for row in cur.fetchall())

        results[2] = result_rows == expected_rows
    else:
        results[2] = False

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
