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

    avg_index = -1 if "average_price" not in result_columns else result_columns.index("average_price")
    result_avg = result_table[0][avg_index] if avg_index != -1 and len(result_table) > 0 else None

    cur.execute("SELECT AVG(price) FROM products;")
    expected_avg = cur.fetchone()[0]

    results = {}

    results[1] = avg_index != -1
    results[2] = (
        avg_index != -1
        and result_avg is not None
        and round(float(result_avg), 2) == round(float(expected_avg), 2)
    )

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
