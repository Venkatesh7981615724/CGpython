# Question 6:
# We have a tuple of numbers given below. Remove the largest number from the tuple and print it in sorted order.
# num_tuple = (5, 8, 13, 2, 17, 1)

num_tuple = (5, 8, 13, 2, 17, 1)
list=[]
for i in num_tuple:
    list.append(i)
list.sort()
print(list[0:-1])
