import sqlite3
import main
import sys
import json

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

try:
    original_non_cancelled = cur.execute(
        "SELECT id FROM orders WHERE status != 'Cancelled' ORDER BY id"
    ).fetchall()

    query = open('query.sql', 'r').read()
    cur.execute(query)

    remaining_cancelled = cur.execute(
        "SELECT COUNT(*) FROM orders WHERE status = 'Cancelled'"
    ).fetchone()[0]
    remaining_non_cancelled = cur.execute(
        "SELECT id FROM orders WHERE status != 'Cancelled' ORDER BY id"
    ).fetchall()

    results = {}
    results[1] = remaining_cancelled == 0
    results[2] = remaining_non_cancelled == original_non_cancelled

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
