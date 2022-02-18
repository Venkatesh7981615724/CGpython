# Question 5:
# I have four variables, each assigned with certain values given below. A massive expression line follows it.
# Re-write the expression which suits the desired lexical model.
# Expected Output:
# 0.4977777777777778

a = 5
b = 2
c = 8
d = 7
x = (((a + b) * (a + c) * (a + d)) / ((b + a) * (b + c) * (b + d)) / ((c + a) * (c + b) * (c + d))) * (a * b * c * d)
print(x)