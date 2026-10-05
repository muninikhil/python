


#sum of first n natural numbers
n=int(input("Enter a number: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Sum of first", n, "natural numbers is:", sum)

#count numbers
i=n
count=0
while i>0:
    count+=1
    i//=10
print("Number of digits in", n, "is:", count)

#check palindrome
num=int(input("Enter a number: "))
temp=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
if temp==reverse:
    print(f"{temp} is a palindrome number")
else:
    print(f"{temp} is not a palindrome number")

#Reverse a Number
n=int(input("Enter a number: "))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print(f"Reverse of the number is: {reverse}")

#factorial of a number
n=int(input("Enter a number: "))
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(f"Factorial of {n} is: {factorial}")