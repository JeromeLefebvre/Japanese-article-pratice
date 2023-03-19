import sqlite3
from datetime import datetime, timedelta

class Learnerdatabase():
    def __init__(self):
        self.conn = sqlite3.connect('learning.sqlite')
        self.c = self.conn.cursor()
        # each character gets a score from 0 to 9.
        # the repetition schedule is to let the algorithm in how many days the character should be practiced again.
        self.repetition_schedule = [0,1,3,7,14,30,60,120,240,365]
        self.table_name = 'recordsv6'

    def create_table(self):
        query = f'''CREATE TABLE {self.table_name} (
            kanji TEXT UNIQUE,
            level INTEGER,
            last_practice DATE
        );'''
        self.c.execute(query)
        self.conn.commit()

    def new_record(self, kanji):
        now = datetime.now()
        # Format the datetime object as a string in the format expected by SQLite
        last_practice = now.strftime('%Y-%m-%d %H:%M:%S')
        level = 0
        query = f"Insert Into {self.table_name} (kanji, level, last_practice) Values ('{kanji}', 0, '{last_practice}')"
        self.c.execute(query)
        self.conn.commit()

    def get_record(self,kanji, create=False):
        # if it doesn't exists, then create the record
        records = self.c.execute(f"select * from {self.table_name} where kanji = '{kanji}'").fetchall()
        if len(records) == 0 and create:
            self.new_record(kanji)
            records = self.c.execute(f"select * from {self.table_name} where kanji = '{kanji}'").fetchall()
        record = records[0]

        record = [record[0], record[1], datetime.strptime(record[2], '%Y-%m-%d %H:%M:%S')]
        return record

    def should_study(self,kanji):
        record = self.get_record(kanji, True)
        now = datetime.now()
        interval = timedelta(self.repetition_schedule[record[1]])

        if ((now - record[2]) > interval):
            return True
        else:
            return False

L = Learnerdatabase()
#L.create_table()

