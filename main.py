# Author: Miles Johnson mcj5246@psu.edu

gradepoint1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")

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
  print(f"Grade point for course 1 is: 4.0")
elif gradepoint1 == "A-":
  print(f"Grade point for course 1 is: 3.67")
elif gradepoint1 == "B+":
  print(f"Grade point for course 1 is: 3.33")
elif gradepoint1 == "B":
  print(f"Grade point for course 1 is: 3.0")
elif gradepoint1 == "B-":
  print(f"Grade point for course 1 is: 2.67")
elif gradepoint1 == "C+":
 print(f"Grade point for course 1 is: 2.33")
elif gradepoint1 == "C":
 print(f"Grade point for course 1 is: 2.0")
elif gradepoint1 == "D":
  print(f"Grade point for course 1 is: 1.0")
elif gradepoint1 == "F":
  print(f"Grade point for course 1 is: 0.0")
else:
    print(f"0.0")


gradepoint2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")

if gradepoint2 == "A":
  print(f"Grade point for course 2 is: 4.0")
elif gradepoint2 == "A-":
  print(f"Grade point for course 2 is: 3.67")
elif gradepoint2 == "B+":
  print(f"Grade point for course 2 is: 3.33")
elif gradepoint2 == "B":
  print(f"Grade point for course 2 is: 3.0")
elif gradepoint2 == "B-":
  print(f"Grade point for course 2 is: 2.67")
elif gradepoint2 == "C+":
 print(f"Grade point for course 2 is: 2.33")
elif gradepoint2 == "C":
 print(f"Grade point for course 2 is: 2.0")
elif gradepoint2 == "D":
  print(f"Grade point for course 2 is: 1.0")
elif gradepoint2 == "F":
  print(f"Grade point for course 2 is: 0.0")
else:
    print(f"0.0")


gradepoint3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")

if gradepoint3 == "A":
  print(f"Grade point for course 3 is: 4.0")
elif gradepoint3 == "A-":
  print(f"Grade point for course 3 is: 3.67")
elif gradepoint3 == "B+":
  print(f"Grade point for course 3 is: 3.33")
elif gradepoint3 == "B":
  print(f"Grade point for course 3 is: 3.0")
elif gradepoint3 == "B-":
  print(f"Grade point for course 3 is: 2.67")
elif gradepoint3 == "C+":
 print(f"Grade point for course 3 is: 2.33")
elif gradepoint3 == "C":
 print(f"Grade point for course 3 is: 2.0")
elif gradepoint3 == "D":
  print(f"Grade point for course 3 is: 1.0")
elif gradepoint3 == "F":
  print(f"Grade point for course 3 is: 0.0")
else:
    print(f"0.0")

gradepoint1 = int(gradepoint1)
gradepoint2 = int(gradepoint2)
gradepoint3 = int(gradepoint3)

credit1 = int(credit1)
credit2 = int(credit2)
credit3 = int(credit3)

GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)

print(f"Your GPA is: {GPA}")