import sqlite3
from src.utils import Utils


class Store:

    def __init__(self):
        self._db_path = Utils.get_full_path('src/store/database.sqlite')
        self._connected = False
        self._connection = None

    def run(self, sql_code, convert=True, columns=[]):
        if self._connected:
            self.close_connection()

        self._connection = self.connect()

        result = self._connection.cursor().execute(sql_code)

        if 'SELECT' in sql_code and convert:
            result = self.convert(table=result, columns=columns)

        self.commit()

        return result

    def commit(self, close_connection=True):
        if not self._connected:
            return

        self._connection.commit()

        if close_connection:
            self.close_connection()

    def close_connection(self):
        if not self._connected:
            return

        self._connection.close()
        self._connected = False

    def connect(self):
        self._connected = True

        return sqlite3.connect(self._db_path)

    def convert(self, table, columns):
        result_table, result_dict = [], {}

        for line in table:
            for i, value in enumerate(line):
                result_dict[columns[i]] = value

            result_table.append(result_dict)
            result_dict = {}

        return result_table

    def select(self, table, columns):
        columns = ', '.join(columns)

        return f'SELECT {columns} FROM {table}'

    def insert(self, table, columns, values):
        values = map(lambda value: f'"{value}"', values)
        values = ', '.join(values)
        columns = ', '.join(columns)

        return f'INSERT INTO {table}({columns}) VALUES({values})'

    def delete(self, table, condition):
        return f'DELETE FROM {table} WHERE {condition}'
