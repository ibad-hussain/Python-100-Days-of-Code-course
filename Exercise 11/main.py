# EXERCISE 11 - DRINK WATER REMINDER
# Problem Statement: Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system.



import time
from plyer import notification

print("Welcome to Drink Water Reminder App!")
time.sleep(1)
name = input("Enter your name: ")
time_sec = int(input("Enter time (in seconds) after you want the reminder: "))
time.sleep(time_sec)
notification.notify(
  title="Reminder",
  message=f"Hey {name}, You need to drink water.",
  app_icon="Alert.ico",
  timeout=7)