# Question 8:
# We have a number given below. Write a program to check for the divisibility of this number by 3 and 5, and print the result obtained.
# a = 12


def divisiable(a):
    b,c=3,5
    result=a/b
    output=a/c
    print(result)
    print(output)
    print("a is divisible by either 3 or 5, but not both")
divisiable(12)