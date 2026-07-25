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

    view_exists = cur.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='view' AND name='shipped_orders'"
    ).fetchone()[0] == 1

    rows_match = False
    if view_exists:
        result_ids = sorted(row[0] for row in cur.execute("SELECT id FROM shipped_orders").fetchall())
        expected_ids = sorted(row[0] for row in cur.execute(
            "SELECT id FROM orders WHERE status = 'Shipped'"
        ).fetchall())
        rows_match = result_ids == expected_ids

    results = {}
    results[1] = view_exists
    results[2] = rows_match

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
