#This Python script counts the time remaining until Valentine's Day

#Imports timedate module from Python
from datetime import datetime

#Print the script's purpose
print("Countdown to Valentine's Day!!!\n")

#Define the function for the countdown
def countdown_to_valentines_day():
    today = datetime.now()
    year = today.year
    valentines_day = datetime(year, 2, 14)
    if today > valentines_day:
      valentines_day = datetime(year + 1, 2, 14)
      message = ("(Valentine's Day has passed for this year.)")
    elif today < valentines_day:
      message = ("(Remember to buy flowers and chocolate!)")
    else:
      message = ("(Buy flowers and chocolate!)")
    countdown = valentines_day - today
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Time left until Valentine's Day: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    print(message)

#Call the function to start the countdown
countdown_to_valentines_day()
