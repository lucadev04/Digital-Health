import app_usage as au
import sqlite3
from sqlite3 import Error


def get_usetimes():
    try:
        formatted_date = au.date_formatter()
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT usetime FROM """+formatted_date
        c = db.cursor()
        c.execute(command)
        usetimes = c.fetchall()
        return usetimes
    except Error as e:
        print(e)
    finally:
        db.close()


def calculate_usetime():
    usetimes = get_usetimes()
    usetime = 0
    for n in usetimes:
        usetime+=int(n[0])
    return usetime

def create_usetime_table():
    try:
        formated_date = au.date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """CREATE TABLE IF NOT EXISTS usetimes (date TEXT PRIMARY KEY,
                                                                usetime INTEGER);"""
        c = db.cursor()
        c.execute(command)
    except Error as e:
        print(e)
    finally:
        db.close()


def insert_usetime(usetime):
    try:
        date = au.date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """INSERT INTO usetimes (date, usetime) VALUES(?,?)"""
        c = db.cursor()
        c.execute(command, (date, usetime))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()


def update_usetime(usetime):
    try:
        date = au.date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """UPDATE usetimes SET usetime = ? WHERE date = ?"""
        c = db.cursor()
        c.execute(command, (usetime, date))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()