import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('learning.sqlite')

# Create a cursor
c = conn.cursor()

# Create record table
table_create = '''CREATE TABLE recordsv3 (
    kanji TEXT UNITQUE,
    xp INTEGER,
    last_practice DATE
);'''

#c.execute(table_create)

# Define the data to be inserted
kanji = '木'
xp = 100
now = datetime.now()

# Format the datetime object as a string in the format expected by SQLite
date_created = now.strftime('%Y-%m-%d %H:%M:%S')
last_practice = date_created

query = f"Insert Into recordsv3 (kanji, xp, last_practice) Values ('{kanji}', {xp}, {last_practice})"
#c.execute(f"Insert Into recordsv3 (kanji, xp, last_practice) Values ('{kanji}', {xp}, '{last_practice}')")
conn.commit()

def get_record(kanji):
    print(f"select * from recordsv3 where")
    a = c.execute(f"select * from recordsv3")    
    print(f"select * from recordsv3 where kanji = '{kanji}'")
    a = c.execute(f"select * from recordsv3 where kanji = '{kanji}'")
    print(a)
    # if there is no reccord, raise alert
    # if not return dict with the values
    pass

get_record('木')

def correct(kanji):
    a = c.execute(f"select * from recordsv3 wheren kanji = 'kanji")
    print(a)
    pass

def incorrect(kanji):
    pass


# Define the data to be inserted
kanji = '木'
xp = 100
now = datetime.now()

# Format the datetime object as a string in the format expected by SQLite
date_created = now.strftime('%Y-%m-%d %H:%M:%S')
last_practice = date_created

query = f"Insert Into recordsv3 (kanji, xp, last_practice) Values ('{kanji}', {xp}, {last_practice})"
print(query)
# Insert the data into the table
c.execute(f"Insert Into recordsv3 (kanji, xp, last_practice) Values ('{kanji}', {xp}, '{last_practice}')")

# Save the changes
conn.commit()

# Close the connection
conn.close()
