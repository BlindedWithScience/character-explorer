import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name, isolation_level=None)
        self.cur = self.con.cursor()

    def query_encoding(self, symbol: str) -> int:
        self.cur.execute("SELECT encoding FROM utf8_encodings WHERE symbol=?", (symbol,))
        result = self.cur.fetchone()

        if result == None:
            raise KeyError()

        return result[0]

    def query_symbol(self, encoding: int) -> str:
        self.cur.execute("SELECT symbol FROM utf8_encodings WHERE encoding=?", (encoding,))
        result = self.cur.fetchone()

        if result == None:
            raise KeyError()

        return result[0]
