import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name, isolation_level=None)
        self.cur = self.con.cursor()

    def query_encoding(self, character: str) -> int:
        """Returns an encoding of a passed character.
        Raises KeyError if there is no such character
        """
        self.cur.execute("SELECT encoding FROM utf8_encodings WHERE symbol=?", (character,))
        result = self.cur.fetchone()

        if result == None:
            raise KeyError()

        return result[0]

    def query_character(self, encoding: int) -> str:
        """Returns a character which a passed encoding represents.
        Raises KeyError if there is no such character
        """
        self.cur.execute("SELECT symbol FROM utf8_encodings WHERE encoding=?", (encoding,))
        result = self.cur.fetchone()

        if result == None:
            raise KeyError()

        return result[0]
