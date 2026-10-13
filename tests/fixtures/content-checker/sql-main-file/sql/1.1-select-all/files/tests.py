import sqlite3
import main
import sys
import json

con = sqlite3.connect(":memory:")
main.setup(connection=con)

try:
    rows = con.execute(open('query.sql', 'r').read()).fetchall()
    sys.stdout.write(json.dumps({1: len(rows) == 2}))
except Exception as e:
    sys.stdout.write(json.dumps({}))
