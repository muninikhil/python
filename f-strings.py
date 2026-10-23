# f-strings are a way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. This makes it easy to create dynamic strings that include variable values or expressions. 
#printing a variable using f-string
name="nikhil"
print(f"my name is {name}")

#using multiple variables in f-string
age=21
city="bangalore"
print(f"my name is{name}, Iam {age} years old and i live in {city}")

#adding two numbers in f-string
a=10
b=20
print(f"the sum of{a} and {b} is{a+b}")

#billing using f-strings
item = "Laptop"
price = 50000
quantity = 2
total_price= price * quantity
print(f"Item: {item}\nPrice: {price}\nQuantity: {quantity}\nTotal Price: {total_price}")

#decimal formatting using f-strings
c=3.141592653589793
print(f"Value of pi: {c:.2f}") 
print(f"Value of pi: {c:.4f}")


