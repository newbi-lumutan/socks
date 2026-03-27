import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        columns_with_types = ', '.join([f'{col} {dtype}' for col, dtype in columns.items()])
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});'
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        sql = f'INSERT INTO {table_name} VALUES ({placeholders})'
        self.cursor.execute(sql, list(data.values()))
        self.connection.commit()

    def close(self):
        self.connection.close()