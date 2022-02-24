# Question 9:
# We have the marks of a student in each subject given below. Write a Python function that takes two parameters 'name' and 'subjects_marks.' Finally, print the student's name and all the subjects in which his/her marks are above 60. If the 'name' is not provided, print 'None.'
# Mathematics = 80, Physics = 58, Chemistry = 62, English = 72, Biology = 50
# Expected Output:
# Name: Brandon - Subjects: {'Chemistry', 'English', 'Mathematics'}


def student_details(name = "none", **kwsubjects):
    subjects=[]
    for key , value in kwsubjects.items():
        if value >60:
            subjects.append(key)
    print("name :{} - subjects:{}".format(name,set(subjects)))
student_details("Brandom",Mathematics = 80, Physics = 58, Chemistry = 62, English = 72, Biology = 50)