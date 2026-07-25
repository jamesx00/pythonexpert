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

    total_index = -1 if "total_quantity" not in result_columns else result_columns.index("total_quantity")
    result_total = result_table[0][total_index] if total_index != -1 and len(result_table) > 0 else None

    cur.execute("SELECT SUM(quantity) FROM order_items;")
    expected_total = cur.fetchone()[0]

    results = {}

    results[1] = total_index != -1
    results[2] = total_index != -1 and result_total is not None and int(result_total) == int(expected_total)

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
