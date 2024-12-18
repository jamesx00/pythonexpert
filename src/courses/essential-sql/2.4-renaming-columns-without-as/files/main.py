import sqlite3
import os
from faker import Faker
from prettytable import from_db_cursor, MARKDOWN
from enum import Enum

def setup(connection):
    fake = Faker()
    Faker.seed(0)

    cur = connection.cursor()

    cur.execute("CREATE TABLE customers(first_name, last_name, age, gender)")

    class Gender(Enum):
        M = "M"
        F = "F"

    for i in range(10):
        cur.execute(
            "INSERT INTO customers (first_name, last_name, age, gender) VALUES (?, ?, ?, ?)", 
            (
                fake.first_name(),
                fake.last_name(), 
                fake.pyint(max_value=80) + 20, 
                fake.enum(Gender).value)
            )

if __name__ == "__main__":
    
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    setup(connection=con)
    query = open('query.sql', 'r').read()
    try:
        res = cur.execute(query)
        table = from_db_cursor(cur)
        print(table)
    except Exception as e:
        print("Error:", str(e))