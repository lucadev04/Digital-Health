import app_usage as au
import time


if __name__ == '__main__':
    au.create_config()
    au.create_table()
    while True:
        active_app = au.get_active_app()
        active_app_id = au.generate_id(au.get_active_app())
        print("active application:", active_app_id)
        apps = au.get_apps()
        print(apps)
        for n in apps:
            print(n)
            print(active_app_id)
            if n == active_app_id:
                usetime_old = au.get_usetime(n)
                usetime_new = 10
                usetime = int(usetime_old[0]) + usetime_new
                au.update_data(usetime, n)
                print("yes")
            else:
                au.insert_data(active_app_id, active_app, 10, 0)
                print("no")
        time.sleep(10)

