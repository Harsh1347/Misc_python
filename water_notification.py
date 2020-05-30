import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title = "Time to drink water",
            message = "You need atleast 3 litres of water daily",
            app_icon = "data\icon.ico",
            timeout = 10

        )
        time.sleep(60*30)