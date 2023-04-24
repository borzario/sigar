import sqlite3 as sq
import list_of_admins
from create_bot import *


def db_start():
    global base, cur
    base = sq.connect("tarakan.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS users1(user_id TEXT PRIMARY KEY, type TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS admins(user_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS call(name TEXT, contact TEXT, time TEXT, status TEXT)')
    base.commit()


async def user_add(message):
    try:
        cur.execute("INSERT INTO users1 VALUES (?, ?)", (message.from_user.id, message.text))
        print(f"add user {message.from_user.id}")
    except:
        print("user was added early")
    base.commit()


async def get_admins_list() -> list:
    return [i[0] for i in cur.execute("SELECT * FROM admins").fetchall()]


async def add_call_to_user(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO call VALUES (?, ?, ?, ?)", tuple([data["name"], data["contact"], data["time"], None]))
        base.commit()
        for i in list_of_admins.admins:
            await bot.send_message(i, f"Заказа звонка №{cur.execute('SELECT MAX(ROWID) from call').fetchall()[0][0]}, ot "
                                      f"{data['name']} {data['contact']} na {data['time']}")


async def get_all_calls(message):
    all_calls = cur.execute("SELECT ROWID, * FROM call").fetchall()
    for i in all_calls:
        await bot.send_message(message.from_user.id, f"№ {i[0]}, name {i[1]}, contact {i[2]}, time {i[3]},"
                                                     f" status {i[4]}")


async def get_new_calls(message):
    all_calls = cur.execute("SELECT ROWID, * FROM call WHERE status IS NULL").fetchall()
    for i in all_calls:
        await bot.send_message(message.from_user.id, f"№ {i[0]}, name {i[1]}, contact {i[2]}, time {i[3]}")


async def close_call(message, call_number):
    cur.execute(f"UPDATE call SET status == ? WHERE ROWID == {call_number}", (f"closed",))
    base.commit()
    await bot.send_message(message.from_user.id, f"position number {call_number} is closed")
