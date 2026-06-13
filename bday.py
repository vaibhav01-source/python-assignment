from datetime import date
bday = input("enter date DD-MM")
day,month = map(int ,bday.split("-"))
today=date.today()
year= today.year

next_bday = date(year,month,day)
if next_bday == today:
    print("Happy Birthday")
elif next_bday > today:
    difference = next_bday - today
    print(" your birthday in %d days" %difference.days)
else:
    next_bday = date(year+1,month,day)
    difference = next_bday - today
    print(" your birthday in {} days".format(difference.days))