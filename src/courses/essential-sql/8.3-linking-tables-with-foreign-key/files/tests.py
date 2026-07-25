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

    foreign_keys = cur.execute("PRAGMA foreign_key_list(reviews)").fetchall()
    matches = [
        fk for fk in foreign_keys
        if fk[2].lower() == "products" and fk[3].lower() == "product_id"
    ]

    results = {}
    results[1] = len(matches) >= 1

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
