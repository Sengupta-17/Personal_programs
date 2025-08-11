import pandas as pd
name=input("Enter student name:")
subjects=["Maths","Science","English"]
marks=[]
for subject in subjects:
    score=int(input(f"Enter marks scored in {subject}:"))
    marks.append(score)

#create a dataframe
df=pd.DataFrame({'Subject': subjects,'Marks':marks})
df.loc['Total']=['Total',sum(marks)]
percentage=sum(marks)/len(subjects)

#garde logic
if percentage >=90:
    grade='A'
elif percentage>=75:
    grad='B'
elif percentage>=50:
    grade='C'
else:
    grade='Fail'

#display table
print("\n-----Student Makrs Report-----")
print(df)
print(f"\nPercentage: {percentage:.2f}%")
print(f"Grade: {grade}")