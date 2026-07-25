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

    avg_index = -1 if "avg_orders" not in result_columns else result_columns.index("avg_orders")
    result_avg = result_table[0][avg_index] if avg_index != -1 and len(result_table) > 0 else None

    cur.execute("""
        SELECT AVG(order_count)
        FROM (
            SELECT customer_id, COUNT(*) AS order_count
            FROM orders
            GROUP BY customer_id
        ) AS customer_order_counts;
    """)
    expected_avg = cur.fetchone()[0]

    results = {}

    results[1] = avg_index != -1
    results[2] = (
        avg_index != -1
        and result_avg is not None
        and abs(float(result_avg) - float(expected_avg)) < 0.001
    )

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps({}))
