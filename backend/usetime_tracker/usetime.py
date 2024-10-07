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

def get_dates():
    try:
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT date FROM usetimes"""
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
                                                                usetime INTEGER,
                                                                formatted_usetime TEXT,
                                                                day TEXT);"""
        c = db.cursor()
        c.execute(command)
    except Error as e:
        print(e)
    finally:
        db.close()


# inserts an usetime from a day into the table if it doesn't exist already
def insert_usetime(date, usetime, day, formatted_usetime):
    try:
        db = sqlite3.connect("../digitalhealth.db")
        command = """INSERT INTO usetimes (date, usetime, day, formatted_usetime) VALUES(?,?,?,?)"""
        c = db.cursor()
        c.execute(command, (date, usetime, day, formatted_usetime))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()


# updates an existing usetime
def update_usetime(date, usetime, formatted_usetime):
    try:
        db = sqlite3.connect("../digitalhealth.db")
        command = """UPDATE usetimes SET usetime = ?, formatted_usetime = ? WHERE date = ?"""
        c = db.cursor()
        c.execute(command, (usetime, formatted_usetime, date))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()


def table_checker():
    try:
        db = sqlite3.connect('../digitalhealth.db')
        cursor = db.cursor()

        cursor.execute('SELECT COUNT(*) FROM usetimes')
        line_count = cursor.fetchone()[0]

        if line_count == 0:
            print('Table is empty.')
            insert_usetime("test", 0, "test", "test")
        else:
            print("table is already filled")

    except Error as e:
        print(e)
    finally:
        db.close()
