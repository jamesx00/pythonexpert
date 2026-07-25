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

    cat_index = -1 if "category" not in result_columns else result_columns.index("category")
    result_categories = sorted(set(row[cat_index] for row in result_table)) if cat_index != -1 else []
    result_no_duplicates = cat_index != -1 and len(result_table) == len(set(row[cat_index] for row in result_table))

    cur.execute("SELECT DISTINCT category FROM products;")
    expected_categories = sorted(row[0] for row in cur.fetchall())

    results[1] = cat_index != -1
    results[2] = result_no_duplicates and result_categories == expected_categories

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
