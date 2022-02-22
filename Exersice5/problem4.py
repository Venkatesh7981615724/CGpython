# Question 4:
# Write a Python program to find the day of the week of a given date?
# given_date = datetime(2008, 5, 15)

from datetime import datetime
given_date = datetime(2008, 5, 15)
print('{}'.format(given_date.strftime('%a')))