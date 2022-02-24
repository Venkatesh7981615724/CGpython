# Question 7:
# Write a Python function to find 'Mall' from the dictionary 'map_details' given below.
# map_details = {101:'Park', 102:'Zoo', 103:'Mall'}
# Expected Output:
# 103


def get_key(val):
    for i,j in map_details.items():
        if val==j:
            return i

map_details = {101:'Park', 102:'Zoo', 103:'Mall'}
result=get_key('Mall')
print(result)