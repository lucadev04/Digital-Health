from Xlib import X, display
import time
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
    return formated_date


def create_table():
    try:
        formated_date = date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """CREATE TABLE IF NOT EXISTS """+formated_date+""" (appid INTEGER PRIMARY KEY,
                                                                appname TEXT,
                                                                usetime INTEGER,
                                                                max_usage INTEGER);"""
        c = db.cursor()
        c.execute(command)
    except Error as e:
        print(e)
    finally:
        db.close()


def insert_data(appid, appname, usetime, max_usage):
    try:
        formated_date = date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """INSERT INTO """+formated_date+""" (appid, appname, usetime, max_usage) VALUES(?,?,?,?)"""
        c = db.cursor()
        c.execute(command, (appid, appname, usetime, max_usage))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()


def update_data(usetime, appid):
    try:
        formated_date = date_formatter()
        db = sqlite3.connect("../digitalhealth.db")
        command = """UPDATE """+formated_date+""" SET usetime = ? WHERE appid = ?"""
        c = db.cursor()
        c.execute(command, (usetime, appid))
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()


def get_apps():
    try:
        formatted_date = date_formatter()
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT appid FROM """ + formatted_date
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



def get_usetime(appid):
    try:
        formatted_date = date_formatter()
        db = sqlite3.connect('../digitalhealth.db')
        command = """SELECT usetime FROM """+formatted_date+""" WHERE appid = ?"""
        c = db.cursor()
        c.execute(command, (appid,))
        usetime = c.fetchone()
        print(usetime)
        return usetime
    except Error as e:
        print(e)
    finally:
        db.close()


#gets the window which is active and returns the applicationname
def get_active_app():
    disp = display.Display()
    root = disp.screen().root
    window_id = root.get_full_property(disp.intern_atom('_NET_ACTIVE_WINDOW'), 0).value[0]

    window = disp.create_resource_object('window', window_id)
    window.change_attributes(event_mask=X.FocusChangeMask)

    try:
        appname = str(window.get_full_property(disp.intern_atom('WM_CLASS'), 0).value)
    except UnicodeDecodeError:
        appname = b""

    return appname


def get_value(name):
    with open("ids.json", "r") as f:
        data = json.load(f)
        return data[name]


def generate_id(appname):
    id = ""
    splitedname = appname.split("'")[1][:4]
    for letter in splitedname:
        with open("ids.json", "r") as f:
            data = json.load(f)
        for l in data:
            if l == letter:
                id += get_value(l)
    return int(id)



create_table()
apps = get_apps()
# print the name of the active window all 10 seconds and safes the app and usetime into a database
while True:
    active_app = get_active_app()
    active_app_id = generate_id(get_active_app())
    print("active application:", active_app_id)
    apps = get_apps()
    print(apps)
    for n in apps:
        print(n)
        print(active_app_id)
        if n == active_app_id:
            usetime_old = get_usetime(n)
            usetime_new = 10
            usetime = int(usetime_old[0])+usetime_new
            update_data(usetime, n)
            print("yes")
        else:
            insert_data(active_app_id, active_app, 10, 0)
            print("no")
    time.sleep(10)



