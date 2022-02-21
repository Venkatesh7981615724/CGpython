# Question 6:
# Merge the two dictionaries given below.
# myDict1 = {1:'One', 2:'Two', 3:'Three'}
# myDict2 = {4:'Four', 5:'Five', 6:'Six'}


myDict1 = {1:'One', 2:'Two', 3:'Three'}
myDict2 = {4:'Four', 5:'Five', 6:'Six'}

result=myDict1.update(myDict2)
print(result)
print(myDict1)