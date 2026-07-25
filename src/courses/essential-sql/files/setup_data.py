import sqlite3
import os
from faker import Faker
from prettytable import from_db_cursor, MARKDOWN
from enum import Enum


def setup(connection):
    fake = Faker()
    Faker.seed(0)

    cur = connection.cursor()

    cur.execute("CREATE TABLE customers(id, first_name, last_name, age, gender)")

    class Gender(Enum):
        M = "M"
        F = "F"

    for i in range(10):
        cur.execute(
            "INSERT INTO customers (id, first_name, last_name, age, gender) VALUES (?, ?, ?, ?, ?)",
            (
                i + 1,
                fake.first_name(),
                fake.last_name(),
                fake.pyint(max_value=80) + 20,
                fake.enum(Gender).value)
            )

    cur.execute("CREATE TABLE products(id, name, category, price)")

    products = [
        (1, "Wireless Mouse", "Electronics", 19.99),
        (2, "Bluetooth Speaker", "Electronics", 45.50),
        (3, "Yoga Mat", "Fitness", 25.00),
        (4, "Running Shoes", "Fitness", 60.00),
        (5, "Coffee Mug", "Home", 8.50),
        (6, "Desk Lamp", "Home", 22.00),
        (7, "Notebook", "Office", 3.50),
        (8, "Backpack", "Office", 40.00),
    ]

    cur.executemany("INSERT INTO products (id, name, category, price) VALUES (?, ?, ?, ?)", products)

    cur.execute("CREATE TABLE orders(id, customer_id, order_date, status, shipped_date)")

    class Status(Enum):
        PENDING = "Pending"
        SHIPPED = "Shipped"
        DELIVERED = "Delivered"
        CANCELLED = "Cancelled"

    order_count = 20
    for i in range(order_count):
        status = fake.enum(Status).value
        order_date = fake.date_between(start_date="-1y", end_date="today")
        shipped_date = None
        if status in ("Shipped", "Delivered"):
            shipped_date = fake.date_between(start_date=order_date, end_date="today").isoformat()

        cur.execute(
            "INSERT INTO orders (id, customer_id, order_date, status, shipped_date) VALUES (?, ?, ?, ?, ?)",
            (
                i + 1,
                fake.pyint(min_value=1, max_value=10),
                order_date.isoformat(),
                status,
                shipped_date)
            )

    cur.execute("CREATE TABLE order_items(id, order_id, product_id, quantity, unit_price)")

    item_id = 1
    for order_id in range(1, order_count + 1):
        item_count = fake.pyint(min_value=1, max_value=3)
        for _ in range(item_count):
            product_id = fake.pyint(min_value=1, max_value=len(products))
            unit_price = products[product_id - 1][3]
            cur.execute(
                "INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?, ?)",
                (
                    item_id,
                    order_id,
                    product_id,
                    fake.pyint(min_value=1, max_value=5),
                    unit_price)
                )
            item_id += 1


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
