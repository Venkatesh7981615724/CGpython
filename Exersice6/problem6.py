# Question 6:
# A list of tuples is given below, containing the candidate's name and their heights(in cm). Sort this list using Lambda functions according to the heights of the candidates.
# candidate_details = [('Harry', 168), ('Jhonny', 160), ('Brad', 178), ('Chris', 172)]
#[('Jhonny', 160), ('Harry', 168), ('Chris', 172), ('Brad', 178)]


candidate_details = [('Harry', 168), ('Jhonny', 160), ('Brad', 178), ('Chris', 172)]
result=[]
for i in range(0,len(candidate_details)-1):
    x,y=candidate_details[i],candidate_details[i+1]
    result.append([y,x])
print(result)
