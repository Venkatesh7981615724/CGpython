# Question 1:
# We have defined a variable x equals 2. Then we have the if-else condition, which checks if x is equal to 2 or not. But we get an error in the output. Decode the error and rectify the program to get the expected output.
# Expected Output:
# Exact match!
try:
    x=int(input("Enter the Number :"))
    if x==2:
        print("Exact match!")
except Exception as e:
    print("please provide the valid input",e)