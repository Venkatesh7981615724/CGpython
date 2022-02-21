# Question 10:
# Print the number and the cube of that number in a dictionary from 0 to 5.
# Expected Output:
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

d=dict()
for x in range(0,6):
    d[x]=x**3
print(d)