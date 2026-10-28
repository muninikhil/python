class person:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"hello {self.name} !")

s1=person("nikhil")
s1.greet()

class caliculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def mul(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2        

c1=caliculator(10,5)
print("addition:",c1.add())
print("subtraction:",c1.sub())
print("multiplication:",c1.mul())
print("division:",c1.div())

class number:
    def __init__(self,num):
        self.num=num

    def even(self):
        if self.num%2==0:
            print(f"{self.num} is even number")
        else:
            print(f"{self.num} is odd number")
n1=number(39)
n2=number(40)
n1.even()
n2.even()