#This Python script counts the time remaining until Valentine's Day

#Print the script's purpose
print ("Countdown to Valentine's Day")

#Imports timedate module from Python
from datetime import datetime

#Defining the function for the countdown
def countdown_to_valentines_day():
    today = datetime.now()  # Gets the current date and time
    year = today.year  # Extracts the current year
    
    # Define the date for Valentine's Day
    valentines_day = datetime(year, 2, 14)

    # Check if Valentine's Day has already passed this year
    if today > valentines_day:
      valentines_day = datetime(year + 1, 2, 14)
      print("(Valentine's Day has passed)")

    if today < valentines_day:
      print("(Remember to buy flowers and chocolate!)")

    if today == valentines_day:
      print("(Buy flowers and chocolate!)")

    # Calculate the time remaining
    countdown = valentines_day - today
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Print the countdown
    print(f"Time left until Valentine's Day: {days} days, {hours} hours, {minutes} minutes, {seconds}, seconds.")

# Call the function to start the countdown
countdown_to_valentines_day()