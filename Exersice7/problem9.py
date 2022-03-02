# Question 9:
# Write a program to square the number entered by the user. But what if the user enters a string or an alphanumeric value, or if some other unexpected exceptions occur. So, wrap the program inside the try-except block to handle the exceptions, and the program should run until the user enters a numeric value.
# Expected Output:
# Enter a number: aa
# Enter a valid input.
# Enter a number: 5
# 25

while True:
    try:
        UserNum = input("Enter a Number: ")
        if UserNum.isdigit() == False:
            raise ValueError
        else:
            UserNum = int(UserNum)
            print(UserNum**2)
            break
    except ValueError:
        print("Enter a valid input.")