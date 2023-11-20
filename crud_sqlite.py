import sqlite3


class BiodataAdmin:
    def __init__(self, name="biodata.db"):
        self.con = sqlite3.Connection(name)

    def table_exists(self):
        sql = "SELECT * FROM data"
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)
            cursor.close()
            return True
        except Exception:
            cursor.close()
            return False

    def create_table(self):
        sql_delete = "DROP TABLE IF EXISTS data"
        sql = "CREATE TABLE data(id INTEGER PRIMARY KEY, seq string, typ string, etos integer, organism string)"
        cursor = self.con.cursor()
        cursor.execute(sql_delete)
        cursor.execute(sql)
        self.con.commit()
        cursor.close()

    def delete_all(self):
        sql = "DELETE FROM data"
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        cursor.close()

    def delete_one(self, seq):
        sql = "DELETE FROM data WHERE seq=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (seq,))
        self.con.commit()
        cursor.close()

    def select_one(self, idv):
        sql = "SELECT * FROM data WHERE id=?"
        cursor = self.con.cursor()
        cursor.execute(sql, (idv,))
        record = cursor.fetchone()
        cursor.close()
        return record

    def insert(self, seq, typ, etos, organism):
        sql = "INSERT INTO data (seq, typ, etos, organism) VALUES (?,?,?,?)"
        cursor = self.con.cursor()
        cursor.execute(sql, (seq, typ, etos, organism))
        self.con.commit()
        cursor.close()
