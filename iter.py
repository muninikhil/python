A=[10,20,30,40,50]
x = iter(A)
print(next(x))
print(next(x))
print(next(x))
print(next(x))


B="Hello, World!"
x=iter(B)
print(next(x))
print(next(x))
print(next(x))


C=[1,2,3,]
x=iter(C)
while True:
    try:
        print(next(x))
    except StopIteration:
        break
print("End of iteration")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration 
for num in MyNumbers():
    print(num)