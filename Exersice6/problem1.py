# Question 1:
# Write a Python function to check whether the number given below is present in between 5 to 10 (both included) or not.
# num = 7
# Expected Output:
# 7 is present between 5-10.
def between(num):
    for i in range(5,10):
        if i==num:
            print("7 is present between 5-10")
between(7)