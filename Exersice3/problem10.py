# Question 10:
# We have a list of numbers given below. Print the number, square of the number, and the cube of the number, all in a single list.
# num = [2, 4, 6, 8]
# Expected Output:
# [(2, 4, 8), (4, 16, 64), (6, 36, 216), (8, 64, 512)]

num = [2, 4, 6, 8]

result = [(i,i**2,i**3) for i in num]
print(result)