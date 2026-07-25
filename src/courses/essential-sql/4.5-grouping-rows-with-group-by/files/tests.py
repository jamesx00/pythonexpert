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

    cat_index = -1 if "category" not in result_columns else result_columns.index("category")
    total_index = -1 if "total" not in result_columns else result_columns.index("total")

    result_pairs = []
    if cat_index != -1 and total_index != -1:
        result_pairs = sorted(
            (row[cat_index], int(row[total_index])) for row in result_table
        )

    cur.execute("SELECT category, COUNT(*) FROM products GROUP BY category;")
    expected_pairs = sorted((row[0], int(row[1])) for row in cur.fetchall())

    results = {}

    results[1] = cat_index != -1 and total_index != -1
    results[2] = result_pairs == expected_pairs

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
