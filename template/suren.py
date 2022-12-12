import schedule
import time

def task():
    print("Do task now")

schedule.every().day.at("13:04").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)