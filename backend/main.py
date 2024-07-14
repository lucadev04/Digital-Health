import app_usage as au
import active_window as aw
import config
import time
import asyncio


if __name__ == '__main__':
    config.create_config()
    au.create_table()
    au.insert_data("test", 0, 0)
    while True:
        active_app = aw.get_active_app()
        print("active application:", active_app)
        apps = au.get_apps()
        print(apps)
        for n in apps:
            print(n)
            print(active_app)
            if n == active_app:
                usetime_old = au.get_usetime(n)
                usetime_new = 10
                usetime = int(usetime_old[0]) + usetime_new
                au.update_data(usetime, n)
                print("yes")
            else:
                au.insert_data(active_app, 10, 0)
                print("no")
        time.sleep(10)

