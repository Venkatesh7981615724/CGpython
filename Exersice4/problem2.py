# Question 2:
# Print all the keys of the dictionary given below.
# myDict = {1:'One', 2:'Two', 3:'Three'}
# Expected Output:
# dict_keys([1, 2, 3])

myDict = {1:'One', 2:'Two', 3:'Three'}
list=[]
for key,value in myDict.items():
    list=myDict.keys()
print(list)


