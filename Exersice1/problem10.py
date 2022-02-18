# Question 10:
# I have an examination form that requires the following information.
# Name, Age, Roll Number, and Subjects.
# Declare the parameters mentioned above with a suitable data type, and then assign some values to it, and finally print the result.


def exam_form(**form):
    return form
x=exam_form(Name= "sachin",age= 17,RollNumber=528841,subjetcs=['Maths', 'Physics', 'Chemistry', 'Computer Science', 'English'])
for i,j in x.items():
    print(i,":",j)
