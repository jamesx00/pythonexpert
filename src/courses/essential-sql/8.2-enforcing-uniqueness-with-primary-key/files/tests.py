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

    table_info = cur.execute("PRAGMA table_info(reviews)").fetchall()
    columns = [row[1].lower() for row in table_info]
    pk_columns = [row[1].lower() for row in table_info if row[5] != 0]

    results = {}
    results[1] = all(c in columns for c in ["id", "product_id", "rating", "comment"])
    results[2] = "id" in pk_columns

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
