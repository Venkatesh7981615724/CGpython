# We have a list of several names along with their age. Now, there is a meeting where seats are reserved for senior citizens (age - 45 above). I want to filter out the senior citizens from this list and get a resultant list where we the names of all those who satisfy the criteria.
# passenger_list = {'Ross' : 35,
#          'Thomas': 42,
#          'Rick' : 55,
#          'Ericson' : 51,
#          'Josh' : 45,
#          'Lara' : 50,
#          'Emma' : 38,
#          'Lily' : 46,
#          'Ron' : 41,
#          'Michael' : 47,
#          'Joanna' : 56,
#          'Arthur' : 42}

passenger_list = {'Ross' : 35,'Thomas': 42, 'Rick' : 55, 'Ericson' : 51, 'Josh' : 45,'Lara' : 50,'Emma' : 38,'Lily' : 46,'Ron' : 41,
                   'Michael' : 47,'Joanna' : 56, 'Arthur' : 42}

for i,j in passenger_list.items():
    if j>45:
        print(i)

# {'Rick', 'Lily', 'Ericson', 'Joanna', 'Michael', 'Lara'}


# Question 9:
# Reverse the integer given below.
# n = 5623
# Expected Output:
# 3265

n = 5623
num=str(n)
result=num[::-1]
print(int(result))