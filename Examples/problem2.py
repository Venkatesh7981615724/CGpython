# Write a Python program to print the volume of a cone whose height and diameter are given below. (Take pi = 3.14)
# h = 10
# d = 13
# 442.21666666666664

def Area_cone(h,d,r,pie=3.14):
    volume=pie*(r*r)*h/3
    return volume
result = Area_cone(10,13,6.5)
print(result)