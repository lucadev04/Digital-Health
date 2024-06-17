from datetime import datetime
import sqlite3
from sqlite3 import Error
import json


def date_formatter():
    date = str(datetime.today()).split(' ')[0]
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]
    formated_date = "t" + year + month + day
    with open("/home/luca/Luca/Privat/Python/digitalhealth/config.json", "r") as f:
        data = json.load(f)
        data["Date"] = formated_date
        data2 = json.dumps(data, indent=1)
    with open("/home/luca/Luca/Privat/Python/digitalhealth/config.json", "w") as f2:
        f2.write(data2)
    return formated_date


def create_table():
    try:
        formated_date = date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """CREATE TABLE IF NOT EXISTS """+formated_date+""" (appname TEXT PRIMARY KEY,
                                                                usetime INTEGER,
                                                                max_usage INTEGER);"""
        c = db.cursor()
        c.execute(command)
    except Error as e:
        print(e)
    finally:
        db.close()


def insert_data(appname, usetime, max_usage):
    try:
        formated_date = date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """INSERT INTO """+formated_date+""" (appname, usetime, max_usage) VALUES(?,?,?)"""
        c = db.cursor()
        c.execute(command, (appname, usetime, max_usage))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()


def update_data(usetime, appname):
    try:
        formated_date = date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """UPDATE """+formated_date+""" SET usetime = ? WHERE appname = ?"""
        c = db.cursor()
        c.execute(command, (usetime, appname))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()


def get_apps():
    try:
        formatted_date = date_formatter()
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT appname FROM """ + formatted_date
        c = db.cursor()
        c.execute(command)
        applist = []
        apps = c.fetchall()
        for app in apps:
            print(app[0])
            applist.append(app[0])
        print(applist)
        return applist
    except Error as e:
        print(e)
    finally:
        db.close()



def get_usetime(appname):
    try:
        formatted_date = date_formatter()
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT usetime FROM """+formatted_date+""" WHERE appname = ?"""
        c = db.cursor()
        c.execute(command, (appname,))
        usetime = c.fetchone()
        print(usetime)
        return usetime
    except Error as e:
        print(e)
    finally:
        db.close()


def get_value(name):
    with open("ids.json", "r") as f:
        data = json.load(f)
        return data[name]


def generate_id(appname):
    id = ""
    splitedname = str(appname).split("'")[1][:4]
    for letter in splitedname:
        with open("ids.json", "r") as f:
            data = json.load(f)
        for l in data:
            if l == letter:
                id += get_value(l)
    return int(id)





