# Question 8:
# Write a function to extract the first ten letters of a string passed as an argument. But if the string is less than ten characters long, raise a ValueError and handle it using the message 'Oops! Too short string.'
# Expected Output:
# Oops! Too short string.
try:
    def extract(string):
        for i in range(len(string)):
            if i<10:
                return i
    result=extract("python")
    print(result)
except ValueError as e:
    print("Oops! Too short string.")