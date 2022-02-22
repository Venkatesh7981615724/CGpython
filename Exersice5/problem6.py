# Question 6:
# Write a Python program to calculate the number of days between two given dates.
# date_1 = datetime(2020, 7, 21).date()
# date_2 = datetime(2020, 3, 10).date()

from datetime import datetime
date_1 = datetime(2020, 7, 21).date()
date_2 = datetime(2020, 3, 10).date()
result_date=date_1-date_2
print(result_date)