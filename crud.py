class BiodataAdmin:
    def __init__(self):
        pass

    def create_table(self):
        SQL_DELETE = "DROP TABLE IF EXISTS data"
        SQL = "CREATE TABLE data(id INTEGER PRIMARY KEY, seq string, typ string, etos integer, organism string)"

    def delete_all(self):
        SQL = "DELETE FROM data"

    def delete_one(self, seq):
        SQL = f"DELETE FROM data WHERE seq={seq}"

    def select_one(self, idv):
        SQL = f"SELECT * FROM data WHERE id={idv}"

    def insert(self, sequence, typos, etos, organism):
        SQL = f"INSERT INTO data (seq, typ, etos, organism) VALUES ('{sequence}', '{typos}', '{etos}', '{organism}')"
