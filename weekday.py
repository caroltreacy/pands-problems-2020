# Carol Treacy
# python weekday.py
# Yes, unfortunately today is a weekday
# It is the weekend, yay!


#weekday = float(input("Yes, unfortunately today is a weekday"))
#weekend = float(input("It is the weekend, yay!"))


import datetime
import calendar 

d = datetime. datetime. today()
print ('Today is date:', d)  
 

week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday']   
l=list(map(int, input("Enter date \n eg: 05/05/2019 \n\n").split('/')))
day=datetime.date(l[2],l[1],l[0]).weekday()
print(week_days [day])
# found this program to say what day today is by entering date


#if week_days == (Monday) #, "Tuesday", "Wednesday", "Thursday", "Friday")
 #  print ("Yes, unfortunately today is a weekday")
#elif week_days == ["Saturday", "Sunday"] 
 #  print ("It is the weekend, yay!") 
# decides if the day is a weekend/weekday




   
