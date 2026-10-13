def setup(connection):
    connection.executescript(
        "CREATE TABLE products (id INTEGER, name TEXT);"
        "INSERT INTO products VALUES (1, 'pen'), (2, 'ink');"
    )
