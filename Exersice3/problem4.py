# Question 4:
# We have a list of numbers given below. Print the square of these numbers into another list using list comprehension.
# num = [2, 4, 6, 8]


num = [2, 4, 6, 8]
result=map(lambda x:x*x ,num)
print(list(result))