import datetime
from playsound import playsound


alarmHour = int(input("Enter Hours:"))
alarmMinutes = int(input("Enter Minutes:"))
alarmAm = input('am or pm?')

if alarmAm == "pm":
    alarmHour+=12

while True:
    if alarmHour == datetime.datetime.now and alarmMinutes == datetime.datetime.now().minute:
       print("Get your LazyHead up!")
       playsound("Give.mp3")
       break
