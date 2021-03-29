import numpy as np
import datetime as dt

start = dt.date(2021, 1, 4)
end = dt.date(2021, 12, 31)

days = np.busday_count(start, end)
print("total hours per week :",(days*4)/7)
print("hours per day", ((days*4)/7)/days)

overtime_hours_per_day = 0.6
off_days = 81
holidays = 13
overtime_hours_due_planned_activities = 54

working_days = days - off_days

print(days)
print(working_days)

#Часове в работни дни + overtime_hours_due_planned_activities * 0.5 - заради планирани дейности
hours_in_working_days = working_days*overtime_hours_per_day*.5 + overtime_hours_due_planned_activities*.5
print("hours_in_working_days :", hours_in_working_days)

#Часове в почивни дни + overtime_hours_due_planned_activities * 0.5 - заради планирани дейности
hours_in_off_days = off_days*overtime_hours_per_day*.5 + overtime_hours_due_planned_activities*.5
print("hours_in_off_days :", hours_in_off_days)

#Часове в празнични дни
hours_in_holiday_days = holidays*overtime_hours_per_day*.5
print("hours_in_holiday_days :",hours_in_holiday_days)

#Нощни часове в работни дни
night_hours_in_working_days= working_days*overtime_hours_per_day*.25
print("night_hours_in_working_days :",night_hours_in_working_days)

#Нощни часове в почивни дни
night_hours_in_off_days = off_days*overtime_hours_per_day*.25
print("night_hours_in_off_days :",night_hours_in_off_days)

#Нощни часове в празнични дни
night_hours_in_holiday_days = holidays*overtime_hours_per_day*.25
print("night_hours_in_holiday_days :",night_hours_in_holiday_days)



# from datetime import date,timedelta
# fromdate = date(2010,1,1)
# todate = date(2010,3,31)
# daygenerator = (fromdate + timedelta(x + 1) for x in xrange((todate - fromdate).days))
# sum(1 for day in daygenerator if day.weekday() < 5)




