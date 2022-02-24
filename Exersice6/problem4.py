# Question 4:
# We have a list of numbers given below. Write a Python function to print all the odd-indexed items from the list.
# n = [2, 3, 5, 6, 8, 9]
# Expected Output:
# (3, 6, 9)

n = [2, 3, 5, 6, 8, 9]
result=[]
for i in range(len(n)):
  if i%2!=0:
     result.append(n[i])
print(tuple(result))
