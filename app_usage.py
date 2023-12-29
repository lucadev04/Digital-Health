from Xlib import X, display
import time
from datetime import datetime
import sqlite3
from sqlite3 import Error

def create_table():
    try:
        date = str(datetime.today()).split(' ')[0]
        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2]
        formated_date = "t"+year+month+day
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
        date = str(datetime.today()).split(' ')[0]
        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2]
        formated_date = "t"+year+month+day
        db = sqlite3.connect("digitalhealth.db")
        command = """INSERT INTO """+formated_date+"""(appname, usetime, max_usage) VALUES(?,?,?)"""
        c = db.cursor()
        c.execute(command, (appname, usetime, max_usage))
        db.commit()
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

    return app_name.decode('utf-8')


create_table()
# print the name of the active window all 10 seconds and safes the app and usetime into a database
while True:
    active_app = get_active_app()
    print("active application:", active_app)
    insert_data(str(active_app), 10, 0)
    time.sleep(10)



