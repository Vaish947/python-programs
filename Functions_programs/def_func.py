def pattern(row,col):
    for i in range(1,row):
        for j in range(1,col):
            print('*',end=' ')
        print(' ')
pattern(5,5)
pattern(6,6)
pattern(7,7)
##################################
def sayhello():
    print('hello world')
    print('This is the first function')
def add():
    a=int(input('enter no 1'))
    b=int(input('enter no 2'))
    c=a+b
    print('addition is',c)
def area():
    r=float(input('enter radius of circle'))
    a=3.14*r*r
    print('area is',a)
print('before')
sayhello()
print('after')
add()
area()
