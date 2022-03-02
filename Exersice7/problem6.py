# Question 6:
# Write a Python program to find the day of the week for the date given below. Also, we don't know what errors we might encounter while executing the program. So, wrap the code inside a try-except block and handle the exceptions by printing the message 'Oops! An error occurred.'
# given_date = datetime(2010, 6, 12)
# Expected Output:
# Saturday
try:
    from datetime import date
    import calendar
    curr_date = date(2010, 6, 12)
    print(calendar.day_name[curr_date.weekday()])
except Exception as e:
    print("Oops! An error occurred.",e)


