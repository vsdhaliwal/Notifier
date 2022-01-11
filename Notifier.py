from plyer import notification
import time
import datetime
import schedule

x = datetime.datetime.now()
print(x.strftime("%X"))

def thursday():
    notification.notify(
        title = 'Class Reminder',
        app_name = 'Buddy',
        message = 'Message you want to give')

schedule.every().thursday.at('''time you want to give''').do(thursday)

while True:
    schedule.run_pending()
    time.sleep(1)
