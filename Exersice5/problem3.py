# Question 3:
# Print the date in the format given below.
# Day_number Month_name(abbr.) Year - Day_name(abbr.)
# given_date = datetime(2011, 10, 12)

from datetime import datetime
given_date = datetime(2011, 10, 12)
print('{} {} {} -{}'.format(given_date.day,given_date.strftime("%b"),given_date.year,given_date.strftime('%a')))