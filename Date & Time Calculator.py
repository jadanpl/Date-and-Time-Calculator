from datetime import datetime, timedelta
today = datetime.now()
now = today.strftime("%B %Y, %A, %I:%M %p")

def what_is_the_date(date):
    if date == 1 or date == 21 or date == 31:
        dd = str(date) + "st"
        return dd
    elif date == 2 or date == 22:
        dd = str(date) + "nd"
        return dd
    elif date == 3 or date == 23:
        dd = str(date) + "rd"
        return dd
    else:
        dd = str(date) + "th"
        return dd
date = what_is_the_date(today.day)

# is it a leap year?
def what_is_the_year(year):
    if year % 400 ==0:
        return " is a leap year"
    elif year % 100 == 0:
        return " is not a leap year"
    elif year % 4 == 0:
        return " is a leap year"
    else:
        return " is not a leap year"

week = int(input("Enter your duration (in weeks): "))
day = int(input("Enter your duration (in days): "))
hour = int(input("Enter your duration (in hours): "))

future_date_and_time = datetime.now() + timedelta(days=day, hours=hour, weeks=week)
future = what_is_the_date(future_date_and_time.day) + " " + future_date_and_time.strftime("%B %Y, %A, %I:%M %p")

print(f"Now, it is {date} {now}.")
print(f"For your information, {today.year} {what_is_the_year(today.year)}.")
print(f"After {week} week(s), {day} day(s), and {hour} hour(s), it would be {future}")

print("Wanna know the time difference between today and a certain date? Let's the following steps calculate for you!")
occasion = input("Enter the name of the occasion: ").lower()
dd = int(input("Enter your date of that occasion (in digits): "))
mm = int(input("Enter your month of that occasion (in digits): "))
yy = int(input("Enter your year of that occasion (in digits): "))
def numOfDays(date1, date2):
    return (date2 - date1).days
time_difference = numOfDays(today, datetime(yy,mm,dd))
print(f"The time difference between today and your {occasion} in {yy} is {time_difference} days")


