# EXERCISE 2 - GOOD MORNING SIR
# Problem Statement: Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.



# CODE-1

import time

currentTime = time.strftime('%H:%M:%S')
print("Your current time is =", currentTime)
hour_1 = int(time.strftime('%H'))
if(hour_1>=0 and hour_1<=4):
  print("Message = Good Night Sir")
elif(hour_1>4 and hour_1<=12):
  print("Message = Good Morning Sir")
elif(hour_1>12 and hour_1<=16):
  print("Message = Good Afternoon Sir")
elif(hour_1>16 and hour_1<=21):
  print("Message = Good Evening Sir")
else:
  print("Message = Good Night Sir")



# CODE-2
  
hour_2 = int(input("Enter your current time (in hours): "))
if(hour_2>=0 and hour_2<=4):
  print("Message: Good Night Sir")
elif(hour_2>4 and hour_2<=12):
  print("Message: Good Morning Sir")
elif(hour_2>12 and hour_2<=16):
  print("Message: Good Afternoon Sir")
elif(hour_2>16 and hour_2<=21):
  print("Message: Good Evening Sir")
elif(hour_2>21 and hour_2<=24):
  print("Message: Good Night Sir")
else:
  print (" ")
  print("Invalid input")