from Xlib import X, display
import time
from datetime import datetime
import sqlite3
from sqlite3 import Error


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
        db = sqlite3.connect("digitalhealth.db")
        command = """CREATE TABLE IF NOT EXISTS """+formated_date+"""(appname TEXT PRIMARY KEY,
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
        db = sqlite3.connect("digitalhealth.db")
        command = """INSERT INTO """+formated_date+"""(appname, usetime, max_usage) VALUES(?,?,?)"""
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
        db = sqlite3.connect("digitalhealth.db")
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
        db = sqlite3.connect('digitalhealth.db')
        command = """SELECT appname FROM """+formatted_date
        c = db.cursor()
        c.execute(command)
        apps = c.fetchall()
        return apps
    except Error as e:
        print(e)
    finally:
        db.close()

def get_usetime(appname):
    try:
        formatted_date = date_formatter()
        db = sqlite3.connect('digitalhealth.db')
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



#gets the window which is active and returns the applicationname
def get_active_app():
    disp = display.Display()
    root = disp.screen().root
    window_id = root.get_full_property(disp.intern_atom('_NET_ACTIVE_WINDOW'), 0).value[0]

    window = disp.create_resource_object('window', window_id)
    window.change_attributes(event_mask=X.FocusChangeMask)

    try:
        app_name = window.get_full_property(disp.intern_atom('WM_CLASS'), 0).value
    except UnicodeDecodeError:
        app_name = b""

    return app_name


create_table()
# print the name of the active window all 10 seconds and safes the app and usetime into a database
while True:
    active_app = get_active_app()
    print("active application:", active_app)
    apps = get_apps()
    for n in apps:
        app = str(n).replace('(', '').replace(')', '').replace('"', '').replace(',', '').replace('\\x00', '\x00')
        print(app)
        insert_data(str(active_app), 10, 0)
        usetime = get_usetime(app)
        usetime_new = usetime+10
        update_data(usetime_new, n)
    time.sleep(10)



