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

    min_index = -1 if "min_price" not in result_columns else result_columns.index("min_price")
    max_index = -1 if "max_price" not in result_columns else result_columns.index("max_price")

    result_min = result_table[0][min_index] if min_index != -1 and len(result_table) > 0 else None
    result_max = result_table[0][max_index] if max_index != -1 and len(result_table) > 0 else None

    cur.execute("SELECT MIN(price), MAX(price) FROM products;")
    expected_min, expected_max = cur.fetchone()

    results = {}

    results[1] = (
        min_index != -1
        and result_min is not None
        and round(float(result_min), 2) == round(float(expected_min), 2)
    )
    results[2] = (
        max_index != -1
        and result_max is not None
        and round(float(result_max), 2) == round(float(expected_max), 2)
    )

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
