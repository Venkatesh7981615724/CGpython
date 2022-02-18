# Question 1:¶
# There are two numbers given below. Print the sum of these numbers if their product is greater than 100. Otherwise, print their product.
# a = 15
# b = 12
def sum_product(a,b):
    sum=a+b
    prod=a*b
    if prod > 100:
        print("the product is ",prod)
        print("the sum is",sum)
sum_product(15,12)
