import schedule
# import helper
import time

def task():
    print("Doing task....",time.strftime("%X (%d %m %y)"))


schedule.every(60).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)