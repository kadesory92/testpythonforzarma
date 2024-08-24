from db.dbConnect import connect

conn = connect()

cursor = conn.cursor()


def getUsers():
    global name, age
    query = "SELECT name, age FROM users WHERE age > 30"
    cursor.execute(query)
    users = cursor.fetchall()

    for user in users:
        name, age = user

    print(f"Name: {name}, Age: {age}")
