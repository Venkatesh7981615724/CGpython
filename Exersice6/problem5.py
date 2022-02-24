# Question 5:
# We have the names of six countries given below. Write a Python function to print all the countries that start with the letter 'A.'
# 'Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran'
# Expected Output:
# ['Austraiia', 'Austria', 'America']


def find(x):
    result=[]
    for i in x:
        if i.startswith('A'):
            result.append(i)
    return result
output=find(['Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran'])
print(output)


