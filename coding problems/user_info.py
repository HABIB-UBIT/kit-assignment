from datetime import datetime, date
name = input("Enter your name")
dob = input("Enter your Date of Birth in MM/DD/YYYY format").strip()
height_in_feet = int(input("Enter your height in feet: "))
height_in_inches = int(input("Enter your height in inches: "))
weight_in_kg = float(input("Enter your weight in kilograms: "))
weight_lb = weight_in_kg * 2.20462
height_cm = (height_in_feet * 12 + height_in_inches) * 2.54
dob = datetime.strptime(dob, "%m/%d/%Y")
age = (datetime.now() - dob).days // 365
print(f"Your age is {age} years.")
today= date.today()
upcoming_birthday = date(today.year, dob.month, dob.day)
if upcoming_birthday < today:
    upcoming_birthday = date(today.year + 1, dob.month, dob.day)
days_until_birthday = (upcoming_birthday - today).days
print(f"Your next birthday is in {days_until_birthday} days.")
print(f"Your weight is {weight_lb:.2f} lb.")
print(f"Your height is {height_cm:.2f} cm.")
if (days_until_birthday < 90):
    print('Happy birthday buddy')
else:
    print('Come on man your birth day is more than 3 months away')