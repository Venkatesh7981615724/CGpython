# Question 2:
# Write a Python function that accepts two arguments and calculates the addition and subtraction of it. Also, print both the arithmetic results in a single return call.
# Expected Output:
# (Addition, Substraction) : (50, 30)

def add_sub(x,y):
    output1=x+y
    output2=x-y
    print("(addition,substraction) : {} {}".format(output1,output2))
add_sub(40,10)