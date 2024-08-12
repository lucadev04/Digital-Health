import app_usage as au
import sqlite3
from sqlite3 import Error


# function for getting all usetimes from the database
def get_app_usetimes():
    try:
        formatted_date = au.date_formatter()
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT usetime FROM """ + formatted_date
        c = db.cursor()
        c.execute(command)
        usetimes = c.fetchall()
        return usetimes
    except Error as e:
        print(e)
    finally:
        db.close()

def get_usetimes():
    try:
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT usetime FROM usetimes"""
        c = db.cursor()
        c.execute(command)
        usetimes = c.fetchall()
        return usetimes
    except Error as e:
        print(e)
    finally:
        db.close()


# adds all usetimes from get usetimes
def calculate_usetime():
    usetimes = get_app_usetimes()
    usetime = 0
    for n in usetimes:
        usetime += int(n[0])
    return usetime


# creates the database table where all usetimes will be stored
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


# inserts an usetime from a day into the table if it doesn't exist already
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


# updates an existing usetime
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
