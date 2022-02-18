# Print the odd indexed elements from the list of colors given below.
# myList = ['Red', 'Blue', 'Orange', 'White', 'Black', 'Yellow']


myList = ['Red', 'Blue', 'Orange',  'White', 'Black', 'Yellow']
even_list=[]
odd_list=[]
for i in range(len(myList)):
    if i%2!= 0:
        odd_list.append(myList[i])

print(odd_list)