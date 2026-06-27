import sqlite3


class SQLiteMemory:

    def __init__(self, db_name="memory.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            query TEXT,
            response TEXT
        )
        """)

        self.conn.commit()

    def save_conversation(self, customer_name, query, response):

        self.cursor.execute("""
        INSERT INTO conversations(customer_name, query, response)
        VALUES (?, ?, ?)
        """, (customer_name, query, response))

        self.conn.commit()

    def get_last_conversation(self, customer_name):

        self.cursor.execute("""
        SELECT query, response
        FROM conversations
        WHERE customer_name = ?
        ORDER BY id DESC
        LIMIT 1
        """, (customer_name,))

        return self.cursor.fetchone()