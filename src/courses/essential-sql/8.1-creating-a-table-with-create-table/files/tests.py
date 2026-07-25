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

    table_exists = cur.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='reviews'"
    ).fetchone()[0] == 1

    columns = []
    if table_exists:
        columns = [row[1].lower() for row in cur.execute("PRAGMA table_info(reviews)").fetchall()]

    results = {}
    results[1] = table_exists
    results[2] = all(c in columns for c in ["id", "product_id", "rating", "comment"])

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
