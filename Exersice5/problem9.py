# Question 9:
# Write a Python program to print yesterdays' date.
# Expected Output:
# Yesterday : 2020-10-16

from datetime import datetime,timedelta
today = datetime.today()
yesterday = today - timedelta(days = 1)
print("Yesterday was: ", yesterday)