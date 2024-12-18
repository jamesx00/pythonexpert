import sqlite3
import main
import sys
import json
from prettytable import from_db_cursor, MARKDOWN

con = sqlite3.connect("tutorial.db")
main.setup(connection=con)
cur = con.cursor()

def compare_column(df_1, df_2, col_1, col_2, test_col):
    """
    Test that the same column of two dataframes share the same values
    """
    col_index_1 = -1 if test_col not in col_1 else col_1.index(test_col)

    if col_index_1 == -1:
        return False

    val_from_df_1 = [row[col_index_1] for row in df_1]

    col_index_2 = -1 if test_col not in col_2 else col_2.index(test_col)

    if col_index_2 == -1:
        return False

    val_from_df_2 = [row[col_index_2] for row in df_2]

    return val_from_df_1 == val_from_df_2

results = {
    3: False,
}

with open('query.sql', 'r') as file:
    content = file.read()
    if " as " not in content.lower():
        results[3] = True

try:
    query = open('query.sql', 'r').read()
    cur.execute(query)
    result_columns = [] if cur.description is None else [c[0] for c in cur.description]
    result_table = cur.fetchall()

    cur.execute("SELECT first_name AS name, last_name AS lastName FROM customers;")
    test_columns = [] if cur.description is None else [c[0] for c in cur.description]
    test_table = cur.fetchall()

    

    results[1] = compare_column(result_table, test_table, result_columns, test_columns, "name")
    results[2] = compare_column(result_table, test_table, result_columns, test_columns, "lastName")

    sys.stdout.write(json.dumps(results))
except Exception as e:
    sys.stdout.write(json.dumps(results))