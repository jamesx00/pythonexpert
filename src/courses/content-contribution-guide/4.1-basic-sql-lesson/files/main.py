import sqlite3
import os
from faker import Faker
from prettytable import from_db_cursor, MARKDOWN

fake = Faker()
Faker.seed(0)

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")

query = open('query.sql', 'r').read()
res = cur.execute(query)
con.commit()

cur.execute("SELECT title, year, score FROM movie")
table = from_db_cursor(cur)
print(table)