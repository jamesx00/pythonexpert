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

    order_items_exists = cur.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='order_items'"
    ).fetchone()[0] == 1
    other_tables = sorted(row[0] for row in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name IN ('customers', 'products', 'orders')"
    ).fetchall())

    results = {}
    results[1] = not order_items_exists
    results[2] = other_tables == ["customers", "orders", "products"]

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
