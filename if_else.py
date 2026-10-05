a=10
if a>0:
    print(f"a is a positive number {a}") 
else:
    print(f"a is a negative number {a}")

#vote eligibility
age=int(input("Enter your age: "))
if age>=18:
    print(f"you are eligible for voting as your age is {age}")
else:
    print(f"you are not eligible for voting as your age is {age}")

#checking the largest number
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))
if x>y and x>z:
    print(f"{x} is greater than {y} and {z}")
elif y>x and y>z:
    print(f"{y} is greater than {x} and {z}")
else:
    print(f"{z} is greater than {x} and {y}")

#grade calculation
marks=int(input("Enter your marks: "))
if marks>=90:
    print(f"Your grade is A as your marks are {marks}")
elif marks>=80:
    print(f"Your grade is B as your marks are {marks}")
elif marks>=70:
    print(f"Your grade is C as your marks are {marks}")
elif marks>=60:
    print(f"Your grade is D as your marks are {marks}")
elif marks>=50:
    print(f"Your grade is E as your marks are {marks}")
else:
    print("FAIL")
    