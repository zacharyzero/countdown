#This script generates the amount of time left until National Go Skateboarding Day
print("Days left until National Go Skateboarding Day")

from datetime import datetime

#Defining the function for go_skate_day_countdown
def go_skate_day_countdown():
  today = datetime.now()
  year = today.year

  #Defining the variable for go_skate_day
  go_skate_day = datetime(year, 6, 21)

  if today.date() == go_skate_day.date():
    print("\nToday is National Go Skateboarding Day!")
    return
  elif today > go_skate_day:
    go_skate_day = datetime(year + 1, 6, 21)
    print("\nNational Go Skateboarding Day has passed for this year.")
  else:
    print("\nNational Go Skateboarding Day is coming up!")

  #Countdown the day until go skate day
  countdown = go_skate_day - today
  days = countdown.days
  hours, remainder = divmod(countdown.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)

  #Display the time remaining until go skate day
  print(f"\nTime remaining until National Go Skateboarding Day: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds!")

#Call the function to countdown the days 
go_skate_day_countdown()


  
  
  


  
  
  
