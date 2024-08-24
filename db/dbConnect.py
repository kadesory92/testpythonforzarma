import sqlite3


# Подключение к базе данных
def connect():
    db_path = "db/data.db"
    conn = sqlite3.connect(db_path)
    return conn


# Создание таблиц
def createTable():
    cursor = connect()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER, name TEXT, age INTEGER)")


# Вставка данных в таблицу.
def insert():
    # cursor = connect()
    conn = connect()

    cursor = conn.cursor()

    cursor.execute("INSERT INTO users VALUES (1, 'Sory', 20)")
    cursor.execute("INSERT INTO users VALUES (2, 'Bana', 30)")
    cursor.execute("INSERT INTO users VALUES (3, 'Kruma', 40)")

    print("Данные были успешно вставлены")

    conn.commit()