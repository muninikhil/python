n=1
for n in range(1, 11):
    print(n)

for n in range(10, 0, -1):
    print(n)

for n in range(1, 21):
    if n%2==0:
        print(n)

for n in range(1, 21):
    if n%2!=0:
        print(n)

x= int(input("Enter a number: "))
for n in range(1, x+1):
    print(n)

y= int(input("Enter a number: "))
for n in range(1,11):
    print(f"{y} x {n} = {y*n}")

z= int(input("Enter a number: "))
for n in range(1, z+1):
    if n%3==0:
        print(f"{n} is a divisible by 3")


for n in range(1, 101):
    if n%5==0 and n%3==0:
        print(f"{n} is a divisible by both 5 and 3")