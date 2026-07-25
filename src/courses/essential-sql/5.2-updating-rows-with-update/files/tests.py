import sqlite3
import main
import sys
import json

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

try:
    original_other_prices = cur.execute(
        "SELECT id, price FROM products WHERE id != 7 ORDER BY id"
    ).fetchall()

    query = open('query.sql', 'r').read()
    cur.execute(query)

    updated_price = cur.execute("SELECT price FROM products WHERE id = 7").fetchone()
    new_other_prices = cur.execute(
        "SELECT id, price FROM products WHERE id != 7 ORDER BY id"
    ).fetchall()

    results = {}
    results[1] = updated_price is not None and abs(updated_price[0] - 4.25) < 0.001
    results[2] = new_other_prices == original_other_prices

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
