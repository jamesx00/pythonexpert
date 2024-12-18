import sqlite3
import main
import sys
import json
from prettytable import from_db_cursor, MARKDOWN

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

try:
    query = open('query.sql', 'r').read()
    res = cur.execute(query)
    result_columns = [] if cur.description is None else [c[0] for c in cur.description]

    results = {}

    results[1] = "first_name" in result_columns

    sys.stdout.write(json.dumps(results))
except:
    sys.stdout.write(json.dumps({}))