import sqlite3
from crypt_func import encode1, decode1
class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS crypt_pass ("
                         "soc_set TEXT NOT NULL,"
                         "password TEXT NOT NULL,"
                         "dop TEXT)")
    def read(self, key: str):
        table = self.cur.execute("SELECT * FROM crypt_pass").fetchall()
        result = []
        for row in table:
            row_res = []
            for i in row:
                row_res.append(decode1(i, key))
            result.append(row_res)
        return result
    def write(self, text : [], key : str):
            self.cur.execute("INSERT INTO crypt_pass (soc_set, password, dop) VALUES (?, ?, ?)", ((encode1(text[0], key)), (encode1(text[1], key)), (encode1(text[2], key))))
            self.connection.commit()
            return True
    def delete(self, data : [], key : str):
        crypted_data = self.cur.execute("SELECT * FROM crypt_pass").fetchall()
        for row in crypted_data:
            if decode1(row[0], key) == data[0] and decode1(row[1], key) == data[1] and decode1(row[2], key) == data[2]:
                self.cur.execute("DELETE FROM crypt_pass WHERE soc_set = (?) AND password = (?) AND dop = (?)", (row[0], row[1], row[2]))
                self.connection.commit()
                break