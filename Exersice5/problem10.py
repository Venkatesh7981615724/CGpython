# Question 10:
# Write a Python program to print the next 5 days from the date given below.
# given_date = datetime(2020, 10, 17)

from datetime import datetime,timedelta
given_date = datetime(2020, 10, 17)

print(given_date+timedelta(days=1))
print(given_date+timedelta(days=2))
print(given_date+timedelta(days=3))
print(given_date+timedelta(days=4))
print(given_date+timedelta(days=5))