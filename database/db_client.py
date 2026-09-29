import sqlite3


class DatabaseClient:

    def __init__(self):
        self.connection = sqlite3.connect("ecommerce.db")
        self.cursor = self.connection.cursor()

    def create_products_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)

        self.connection.commit()

    def add_product(self, product_id, name, price):
        self.cursor.execute(
            """
            INSERT OR REPLACE INTO products (id, name, price)
            VALUES (?, ?, ?)
            """,
            (product_id, name, price)
        )

        self.connection.commit()

    def get_product(self, product_id):
        self.cursor.execute(
            "SELECT id, name, price FROM products WHERE id = ?",
            (product_id,)
        )

        return self.cursor.fetchone()

    def close(self):
        self.connection.close()