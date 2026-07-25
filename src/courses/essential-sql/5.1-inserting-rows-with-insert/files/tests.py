import sqlite3
import main
import sys
import json

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

try:
    original_total = cur.execute("SELECT COUNT(*) FROM products").fetchone()[0]

    query = open('query.sql', 'r').read()
    cur.execute(query)

    new_total = cur.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    matching_rows = cur.execute(
        "SELECT COUNT(*) FROM products WHERE name = ? AND category = ? AND price = ?",
        ("Desk Chair", "Office", 85.00)
    ).fetchone()[0]

    results = {}
    results[1] = new_total == original_total + 1
    results[2] = matching_rows == 1

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
