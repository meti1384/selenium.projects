import schedule
import datetime
from time import sleep
from setting_of_checking_notif import main


target_date = datetime(2024, 5, 20, 15, 30)
schedule.every().day.at(target_date.strftime("%H:%M")).do(main)

while True:
    schedule.run_pending()
    sleep(1)