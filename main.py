# Author: Miles Johnson mcj5246@psu.edu

gradepoint1 = input("Enter your course 1 letter grade: ")
gradepoint2 = input("Enter your course 2 letter grade: ")
gradepoint3 = input("Enter your course 3 letter grade: ")

points = 0
credits = 3

A = 4.0
A_min = 3.67
B_plus = 3.33
B = 3.0
B_min = 2.67
C_plus = 2.33
C = 2.0
D = 1.0
F = 0.0

if gradepoint1 == "A":
  points += A
elif gradepoint1 == "A-":
  points += A_min
elif gradepoint1 == "B+":
  points += B_plus
elif gradepoint1 == "B":
  points += B
elif gradepoint1 == "B-":
  points += B_min
elif gradepoint1 == "C+":
  points += C_plus
elif gradepoint1 == "C":
  points += C
elif gradepoint1 == "D":
  points += D
elif gradepoint1 == "F":
  points += F
else:
    print(f"ERROR")

if gradepoint2 == "A":
  points += A
elif gradepoint2 == "A-":
  points += A_min
elif gradepoint2 == "B+":
  points += B_plus
elif gradepoint2 == "B":
  points += B
elif gradepoint2 == "B-":
  points += B_min
elif gradepoint2 == "C+":
  points += C_plus
elif gradepoint2 == "C":
  points += C
elif gradepoint2 == "D":
  points += D
elif gradepoint2 == "F":
  points += F
else:
    print(f"ERROR")

if gradepoint3 == "A":
  points += A
elif gradepoint3 == "A-":
  points += A_min
elif gradepoint3 == "B+":
  points += B_plus
elif gradepoint3 == "B":
  points += B
elif gradepoint3 == "B-":
  points += B_min
elif gradepoint3 == "C+":
  points += C_plus
elif gradepoint3 == "C":
  points += C
elif gradepoint3 == "D":
  points += D
elif gradepoint3 == "F":
  points += F
else:
    print(f"ERROR")

gpa = points / (credits*4)
print(f"Your GPA is: {gpa}")