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
    result_columns = [] if cur.description is None else [c[0] for c in cur.description]
    result_table = cur.fetchall()

    results = {}

    name_index = -1 if "first_name" not in result_columns else result_columns.index("first_name")
    order_id_index = -1 if "order_id" not in result_columns else result_columns.index("order_id")

    results[1] = name_index != -1 and order_id_index != -1

    if results[1]:
        cur.execute("SELECT first_name FROM customers WHERE id = 1;")
        no_order_customer_name = cur.fetchone()[0]

        matching_rows = [
            row for row in result_table
            if row[name_index] == no_order_customer_name and row[order_id_index] is None
        ]
        results[2] = len(matching_rows) == 1

        cur.execute(
            "SELECT c.first_name, o.id "
            "FROM customers c "
            "LEFT JOIN orders o ON c.id = o.customer_id;"
        )
        expected_rows = cur.fetchall()
        results[3] = len(result_table) == len(expected_rows)
    else:
        results[2] = False
        results[3] = False

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
