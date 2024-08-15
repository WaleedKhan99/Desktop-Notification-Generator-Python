from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = " *** Take Rest *** ",
            message = "It's time to rest and allow your eyes to refresh. Please consider taking a break to relax.",
            app_icon = "G:\Python project\Desktop Notification\Rest Icon.ico",
            timeout = 10)
        time.sleep(60)
            
        