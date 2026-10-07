def function():
    return "Hello, World!"

print(function())

def square(n):
    n=n*n
    return n
x= int(input("Enter a number: "))
print(square(x))

def even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
y = int(input("Enter a number: "))
print(even_odd(y))


def max(a,b):
    if a>b:
        return a
    else:
        return b

z = int(input("Enter the first number: "))
w = int(input("Enter the second number: "))
print(max(z, w))

#arguments and parameters
def add(a,b):
    return a+b
print(add(5, 10))

def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

def calculate(a,b,operator):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b
    else:
        return "Invalid operator"

x= int(input("Enter the first number: "))
y= int(input("Enter the second number: "))
operator= input("Enter the operator (+, -, *, /): ")
result= calculate(x,y,operator)
print(f"The result is: {result}")


def add(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
print(add(5, 10, 15,67,89,34,67))


def multiply(**a):
    product=1
    for i in a.values():
        product*=i
    return product
print(multiply(x=5, y=10, z=15))


def students(**a):
    for key,value in a.items():
        print(f"{key}: {value}")
students(name="Alice", age=20, grade="A")

