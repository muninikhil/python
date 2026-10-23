
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print("The result of division is:", result)
finally:
    print("Execution completed.")




