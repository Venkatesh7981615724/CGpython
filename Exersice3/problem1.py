# Question 1:¶
# Convert the string given below into a list by taking each word separated by a comma as an element.
# languages = "Java, Python, C++, Scala, C"

languages = "Java, Python, C++, Scala, C"
result=list(languages.split(','))
print(result)