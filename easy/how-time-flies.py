#https://www.codingame.com/ide/puzzle/how-time-flies

from datetime import date

begin_d,begin_m,begin_y = map(int, input().split("."))
end_d,end_m,end_y = map(int, input().split("."))

date1 = date(begin_y,begin_m,begin_d)
date2 = date(end_y,end_m,end_d)
diff = date2 - date1
    


days_left = diff.days
if days_left > 1 :
    days_left = "total " + str(days_left) + " days"
elif days_left == 1 :
    days_left = "total " + str(days_left) + " day"


month_left = (diff.days%365)//30
if month_left > 1 :
    month_left = str(month_left) + " months"
elif month_left == 1 :
    month_left = str(month_left) + " month"


years_left = diff.days//365
if years_left > 1 :
    years_left = str(years_left) + " years"
elif years_left == 1 :
    years_left = str(years_left) + " year"

res = []

if diff.days//365 > 0:
    res.append(years_left)
if (diff.days%365)//30 > 0 and diff.days > 30:
    res.append(month_left)
if diff.days != 0:
    res.append(days_left)
else:
    res.append("total 0 days")

print(", ".join(res))