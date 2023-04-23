import sqlite3 as sq

def db_start():
    global base, cur
    base = sq.connect("tarakan.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS users1(user_id TEXT PRIMARY KEY, type TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS admins(user_id TEXT)')
    base.commit()

async def user_add(message):
    try:
        cur.execute("INSERT INTO users1 VALUES (?, ?)", (message.from_user.id, message.text))
        print(f"add user {message.from_user.id}")
    except:
        print("user was added early")
    base.commit()