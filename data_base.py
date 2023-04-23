import sqlite3 as sq

def db_start():
    global base, cur
    base = sq.connect("tarakan.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT, type TEXT)')
    base.commit()

async def user_add(message):
    try:
        await cur.execute("INSERT INTO users VALUES (?, ?)", (message.from_user.id, message.text))
    except:
        pass
    base.commit()