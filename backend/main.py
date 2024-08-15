import app_usage as au
import active_window as aw
import usetime as us
import config
import asyncio
import datetime


if __name__ == '__main__':
    async def appusage():
        config.create_config()
        au.create_table()
        date = au.date_formatter()
        au.table_checker(date)
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
            await asyncio.sleep(10)

    async def usetime():
        while True:
            us.create_usetime_table()
            us.table_checker()
            usetime = us.calculate_usetime()
            formatted_usetime = str(datetime.timedelta(seconds=usetime))
            day = datetime.date.today().strftime('%A')
            date = au.date_formatter()
            dates = us.get_dates()
            for n in dates:
                print(n[0])
                if date == n[0]:
                    us.update_usetime(date, usetime, formatted_usetime)
                    print("date")
                else:
                    us.insert_usetime(date, usetime, day, formatted_usetime)
                    print("not date")
            await asyncio.sleep(10)


    async def main():
        await asyncio.gather(appusage(), usetime())
        print("kek")


    asyncio.run(main())


