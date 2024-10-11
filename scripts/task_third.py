import sqlite3
import os


db_dir = 'D:/projects/pl_test/database'
if not os.path.exists(db_dir):
    os.makedirs(db_dir) # автоматическое создание папки если ее нет по адресу D:/projects/pl_test/database


db_path = os.path.join(db_dir, 'orders.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ORDERS (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    ORDERS_COUNT INTEGER,
    SEND_DATE TEXT
)
''')

orders = [
    (1, 'Книги', 50, '2023-02-01'),
    (2, 'Тетради', 20, '2021-10-15'),
    (3, 'Пеналы', 10, '2022-01-01')
]

cursor.execute("SELECT COUNT(*) FROM ORDERS")  # если тыблица пуста то всиавляем данные
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO ORDERS (ID, NAME, ORDERS_COUNT, SEND_DATE) VALUES (?, ?, ?, ?)", orders)
    conn.commit()

print("База данных и таблица созданы, данные вставлены")

conn.close()
