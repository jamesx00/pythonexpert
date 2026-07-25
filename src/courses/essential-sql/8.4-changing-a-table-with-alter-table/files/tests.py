import sqlite3
import main
import sys
import json

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

try:
    original_count = cur.execute("SELECT COUNT(*) FROM customers").fetchone()[0]

    query = open('query.sql', 'r').read()
    cur.execute(query)

    columns = [row[1].lower() for row in cur.execute("PRAGMA table_info(customers)").fetchall()]
    new_count = cur.execute("SELECT COUNT(*) FROM customers").fetchone()[0]

    results = {}
    results[1] = "email" in columns
    results[2] = new_count == original_count

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
