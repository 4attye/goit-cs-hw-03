import sqlite3 as sql
from faker import Faker

fake = Faker()

con = sql.connect('task_1/database.sqlite')
cur = con.cursor()

statuses = [("new",), ("in progress",), ("completed",)]

for i in range(1, 11):
    cur.execute('INSERT INTO users (id, fullname, email) VALUES (?, ?, ?)', (i, fake.name(), fake.email()))

for i, values in enumerate(statuses, start=1):
    cur.execute('INSERT INTO status (id, name) VALUES (?, ?)', (i, values[0]))

for i in range(1, 31):
    cur.execute('INSERT INTO tasks (id, title, description, status_id, user_id) VALUES (?, ?, ?, ?, ?)', (i, fake.sentence(), fake.text(), fake.random_int(1, 3), fake.random_int(1, 10)))

con.commit()
con.close()
