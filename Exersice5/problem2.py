# Print the month and minutes from the datetime object given below.
# dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)
from datetime import datetime
dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)
print('month:{}'.format(dob_time.month))
print('minute:{}'.format(dob_time.minute))