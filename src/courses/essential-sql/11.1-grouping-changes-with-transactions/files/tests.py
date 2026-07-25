import sqlite3
import main
import sys
import json

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

try:
    original_price = cur.execute("SELECT price FROM products WHERE id = 1").fetchone()[0]

    query = open('query.sql', 'r').read()
    uses_transaction = "begin" in query.lower() and "rollback" in query.lower()

    con.executescript(query)

    final_price = cur.execute("SELECT price FROM products WHERE id = 1").fetchone()[0]

    results = {}
    results[1] = uses_transaction
    results[2] = abs(final_price - original_price) < 0.001

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
