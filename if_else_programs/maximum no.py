a=int(input('enter no 1'))
b=int(input('enter no 2'))
if a>b:
    print('a is maximum')
else:
    print('b is maximum')
###############################
a=int(input('enter no 1'))
b=int(input('enter no 2'))
c=int(input('enter no 3'))
if a>b and a>c:
    print('a is maximum')
elif b>a and b>c:
    print('b is maximum')
else:
    print('c is maximum')