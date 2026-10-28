class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=students("nikhil",21)
s2=students("sachin",22)
print("hello student!",s1.name,"age:",s1.age)
print("hello student!",s2.name,"age:",s2.age)

class employe:
    def __init__(self,emp_name,emp_id,emp_salary):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_salary=emp_salary

e1=employe("nikhil",101,50000)
e2=employe("sachin",102,60000)
e3=employe("rohit",103,70000)
for i in range(1,4):
    print("employee details\nname:",eval(f"e{i}.emp_name"),"\nid:",eval(f"e{i}.emp_id"),"\n salary:",eval(f"e{i}.emp_salary"))


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
s1=rectangle(100,5)
area=s1.length*s1.breadth
print("area of rectangle:",area)