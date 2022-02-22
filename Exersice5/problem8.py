# Question 8:
# Print the date, day name, and time in the format given below.
# Day_number-Month_number-Year - Day_name - Hours:Minutes:Seconds
# dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)

from datetime import datetime
dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)
print('{}-{}-{}'.format(dob_time.strftime('%d-%m-%Y'),dob_time.strftime('%a'),dob_time.strftime("%I:%M:%S")))