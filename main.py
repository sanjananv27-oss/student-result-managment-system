name=input("enter student name: ")
roll_no = input("enter Roll Number: ")

Sub1=int(input("enter marks in subject 1: "))
Sub2=int(input("enter marks in subject 2:" ))
Sub3=int(input("enter marks in subject 3:" ))

total = Sub1 + Sub2 + Sub3
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n-----STUDENT RESULT-----")
print("Name:", name)
print("Roll Number:", roll_no)
print("total marks:", total)
print("percentage:", percentage)
print("Grade:", grade)






