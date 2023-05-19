def add_time(start, duration, day_of_week=None):
    #start = "00:00 AM"
    #duration = "70:00"
    #day_of_week = "Monday"
    new_day_of_week = ""

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
   
    #Get new time hours, minutes
    new_hours = int(new_time_in_minutes / 60)
    new_minutes = new_time_in_minutes % 60

    #if hours is greater than 24 hours then calculate days
    new_days = 0
    if new_hours > 24:
        new_days = int(new_hours / 24)
        new_hours = new_hours % 24


    #Add AM/PM
    ampm_label = "AM"
    if new_hours > 12:
        ampm_label = "PM"
        new_hours = new_hours - 12


    #add next day or ndays label
    text = ''
    if new_days == 1:
        day_label = ' (next day)'
    elif new_days > 1:
        day_label = " (" + str(new_days) + ' days later)'
    else:
        day_label = ''

    #getting the day of the week if provided
    if day_of_week != None:
        offset = (week_days.index(day_of_week.lower()) + new_days) % 7
        new_day_of_week = week_days[offset]
        day_label = " " + new_day_of_week.capitalize() + day_label

    output =  str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + ampm_label + day_label

    return output

