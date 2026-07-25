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
    cur.execute(query)
    result_columns = [] if cur.description is None else [c[0] for c in cur.description]
    result_table = cur.fetchall()

    results = {}

    age_index = -1 if "age" not in result_columns else result_columns.index("age")
    result_ages = [row[age_index] for row in result_table] if age_index != -1 else []

    cur.execute("SELECT age FROM customers ORDER BY age DESC LIMIT 3;")
    expected_ages = [row[0] for row in cur.fetchall()]

    results[1] = age_index != -1
    results[2] = len(result_table) == 3
    results[3] = age_index != -1 and result_ages == expected_ages

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
