import psycopg2
from faker import Faker

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="415263"
)
cur = conn.cursor()

statuses = [("new",), ("in progress",), ("completed",)]

for i in range(1, 11):
    cur.execute('INSERT INTO users (fullname, email) VALUES (%s, %s)', (fake.name(), fake.email()))

for status in statuses:
    cur.execute('INSERT INTO status (name) VALUES (%s)', (status,))

for i in range(1, 31):
    cur.execute('INSERT INTO tasks (title, description, status_id, user_id) VALUES ( %s, %s, %s, %s)', (
        fake.sentence()
        , fake.text()
        , fake.random_int(1, 3)
        , fake.random_int(1, 10)))

conn.commit()
conn.close()
cur.close()
