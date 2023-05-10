import sqlite3 as sq

import keyboard
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
    base.execute('CREATE TABLE IF NOT EXISTS oder(name TEXT, contact TEXT, time TEXT, service TEXT, type TEXT, adress TEXT, discription TEXT,  status TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS order_worker(number TEXT, worker TEXT, status TEXT)')
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
        await bot.send_message(message.from_user.id, f"№ {i[0]}, name {i[1]}, contact {i[2]}, time {i[3]}, "
                                                     f"status {i[4]}")


async def get_new_calls(message):
    all_calls = cur.execute("SELECT ROWID, * FROM call WHERE status IS NULL").fetchall()
    for i in all_calls:
        await bot.send_message(message.from_user.id, f"№ {i[0]}, name {i[1]}, contact {i[2]}, time {i[3]}")


async def close_call(message, call_number):
    cur.execute(f"UPDATE call SET status == ? WHERE ROWID == {call_number}", (f"closed",))
    base.commit()
    await bot.send_message(message.from_user.id, f"position number {call_number} is closed")


async def get_info_about_user(message) -> str:
    return cur.execute(f"SELECT type FROM users1 WHERE user_id == {message.from_user.id}").fetchall()[0][0]


async def add_master_call(state):
    async with state.proxy() as data:
        try:
            cur.execute("INSERT INTO oder VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tuple([data["name"], data["contact"], data["time"], data["service"], data["type"],  data["adress"], data["discription"], None]))
            base.commit()
        except:
            print(tuple([data["name"], data["contact"], data["time"], data["service"], data["type"],  data["adress"], data["discription"], None]))
        for i in list_of_admins.admins:
            await bot.send_message(i, f"Новый заказ № {cur.execute('SELECT MAX(ROWID) from call').fetchall()[0][0]}, "
                                          f"клиент: {data['name']}, контакт: {data['contact']} {data['type']}, время: {data['time']}, "
                                      f"услуга: {data['service']}, описание: {data['discription']}; адрес: {data['adress']}")


async def get_all_oders(message):
    all_oders = cur.execute("SELECT ROWID, * FROM oder").fetchall()
    for i in all_oders:
        await bot.send_message(message.from_user.id, f"№ {i[0]}, name: {i[1]}, contact: {i[2]}, time: {i[3]}, service: {i[4]}, "
                                                     f"type:  {i[5]}, problem: {i[6]}, adress: {i[7]}, status: {i[8]}")


async def get_new_oders(message):
    new_oders = cur.execute("SELECT ROWID, * FROM oder WHERE status IS NULL").fetchall()
    for i in new_oders:
        await bot.send_message(message.from_user.id, f"№ {i[0]}, name: {i[1]}, contact: {i[2]}, time: {i[3]}, service: {i[4]}, "
                                                     f"type:  {i[5]}, problem:  {i[6]}, adress:  {i[7]}")


async def close_oder(message, oder_number: str):
    cur.execute(f"UPDATE oder SET status == ? WHERE ROWID == {oder_number}", (f"closed",))
    base.commit()
    await bot.send_message(message.from_user.id, f"position number {oder_number} is closed")


async def send_order_to_master(state):
    async with state.proxy() as data:
        order: tuple = cur.execute(f"SELECT * FROM oder WHERE ROWID == {data['number']}").fetchall()[0]
        await bot.send_message(data['master'], f"{order}", reply_markup=keyboard.kb_accepting)
        cur.execute(f"INSERT INTO order_worker VALUES (?, ?, ?)", tuple([data['number'], list_of_admins.workers_back[f"{data['master']}"], None]))
        base.commit()

async def accept_order(message):
    m_rowid = cur.execute("SELECT MAX(ROWID) FROM order_worker").fetchall()[0][0]
    content = cur.execute(f"SELECT * FROM order_worker WHERE ROWID == {m_rowid}").fetchall()[0]
    if message.text.lower() == "accept":
        cur.execute(f"UPDATE order_worker SET status == ? WHERE ROWID == {m_rowid}", (f"{message.text}",))
        cur.execute(f"UPDATE oder SET status == ? WHERE ROWID == {content[0]}", (content[1],))
        for i in list_of_admins.admins:
            await bot.send_message(i, "Работяга подписался под заказ")
        base.commit()
    else:
        cur.execute(f"UPDATE order_worker SET status == ? WHERE ROWID == {m_rowid}", (f"{message.text}",))
        for i in list_of_admins.admins:
            await bot.send_message(i, "Работяга слился с заказа")
        base.commit()

async def get_user_type(message):
    return cur.execute(f"SELECT type FROM users1 WHERE user_id == {message.from_user.id}").fetchall()[0][0]

