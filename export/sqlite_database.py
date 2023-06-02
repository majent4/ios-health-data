from sqlite3 import connect as sqlite_connect, Error as sqlite_error
from utils import print_exit

class SQLiteDatabase:
    def __init__(self, db_file):
        try:
            self.conn = sqlite_connect(db_file)
            self.cursor = self.conn.cursor()
        except sqlite_error as e:
            print_exit(f'Error connecting to database: {e}')

    def execute(self, query, parameters=None):
        try:
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
        except sqlite_error as e:
            print_exit(f'Error executing query: {e}')

    def commit(self):
        try:
            self.conn.commit()
        except sqlite_error as e:
            print_exit(f'Error committing changes: {e}')

    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except sqlite_error as e:
            print_exit(f'Error closing database: {e}')

    def create_table_if_not_exists(self, table_name, table_columns):
        try:
            self.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({table_columns})')
            self.commit()
        except sqlite_error as e:
            print_exit(f'Error creating table: {e}')
