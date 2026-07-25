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

    index_names = [row[1] for row in cur.execute("PRAGMA index_list(orders)").fetchall()]

    matched = False
    for index_name in index_names:
        columns = [row[2] for row in cur.execute(f"PRAGMA index_info({index_name})").fetchall()]
        if "customer_id" in columns:
            matched = True

    results = {}
    results[1] = matched

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
