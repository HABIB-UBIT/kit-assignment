from datetime import date , datetime

name= str(input("Name of user"))
dob = input('Enter a date formatted as MM-DD-YYYY: ').split('-') # split('-') is splitting the input on each hyphen
height= float(input("Enter height in ft and inches"))
weight= float(input("Enter weight in kg"))

dob = datetime.datetime.strptime(dob, "%m-%d-%y").date()
height_ft, height_inch = [int(x) for x in height.split("'")]
weight_kg = float(weight)

today= datetime.date.today()
age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
    next_birthday_year = today.year 
else:
     today.year + 1
next_birthday = datetime.date(next_birthday_year, dob.month, dob.day)
days_until_birthday = (next_birthday - today).days

height_cm = (height_ft * 30.48) + (height_inch * 2.54)
weight_lb = weight_kg * 2.20462

if days_until_birthday <= 90:
    print("Happy birthday buddy!")
else:
    print("Come on man, your birthday is more than 3 months away.")



