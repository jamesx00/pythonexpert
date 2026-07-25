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

    results[1] = name_index != -1

    if results[1]:
        result_names = sorted(row[name_index] for row in result_table)

        cur.execute(
            "SELECT name FROM products WHERE category = 'Electronics' "
            "UNION "
            "SELECT name FROM products WHERE category = 'Fitness';"
        )
        expected_names = sorted(row[0] for row in cur.fetchall())

        results[2] = result_names == expected_names
    else:
        results[2] = False

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
