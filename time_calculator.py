import sys
import datetime

#def add_time(start, duration, day_of_week=None):
start = "3:00 PM"
duration = "73:30"
day_of_week = "Monday"

#declare variables
week_days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

#Get start time and duration components
start_meridian_indicator = start.split()[1]
start_hour = int(start.split()[0].split(":")[0])
start_minutes = int(start.split()[0].split(":")[1])
duration_hour = int(duration.split(":")[0])
duration_minutes = int(duration.split(":")[1])

#Adjust time if past meridian time
if start_meridian_indicator == 'PM':
    start_hour = start_hour + 12

#Calculate new time
new_time_in_minutes = (start_hour * 60) + start_minutes + (duration_hour * 60) + duration_minutes
print(new_time_in_minutes)

#Get new time hours, minutes
new_hours = new_time_in_minutes / 60
new_minutes = new_time_in_minutes % 60

print(new_hours)
print(new_minutes)
#if hours is greater than 24 hours then calculate days
new_days = 0
if new_hours > 24:
    new_days = int(int(new_hours) / 24)
    new_hours = int(new_hours) % 24

#Add AM/PM
ampm_label = "AM"
if new_hours > 12:
    ampm_label = "PM"
    new_hours = new_hours - 12


#add next day or ndays label
if new_days == 1:
    day_label = '(next day)'
elif new_days > 1:
    day_label = str(new_days) + ' days later'
else:
    day_label = ''

print(str(new_hours) + ":" + str(new_minutes) + " " + ampm_label + " " + day_label)



#print(start_time_in_minutes)
#check if a valid week_day_value was received
#if day_of_week == None:
#    day_of_week = datetime.datetime.now().strftime("%A")
#    print(day_of_week)
#else:
#    if day_of_week.lower() in week_days:
#        print("wwooooow")
#    else:
#        print("ERROR: Invalid day of Week, value must be any of the following: ", week_days)
#        #sys.exit()

#Build date
#year = 
#month = 
#day = 

    




#    return new_time