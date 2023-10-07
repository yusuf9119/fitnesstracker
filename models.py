import sqlite3

class Fitness:
    def __init__(self):
        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS Fitness""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Fitness (
            date DATE PRIMARY KEY,
            weight REAL,
            calorie_intake REAL,
            Muscles_trained TEXT
        )""")

    def insert(self, item):
        self.cur.execute("""INSERT OR IGNORE INTO Fitness VALUES(?,?,?,?)""", item)
        self.con.commit()

    def read_all(self):
        self.cur.execute("""SELECT * FROM Fitness""")
        rows = self.cur.fetchall()
        return rows

    def close(self):
        self.con.close()