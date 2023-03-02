a=int(input('basic salary of an employee'))
if a<=10000:
    b=a*0.2
    c=a*0.8
    d=a+b+c
    print('gross salary is',d)
elif a<=20000:
    b=0.25*a
    c=0.9*a
    d=a+b+c
    print('gross salary is',d)
elif a>20000:
    b=0.3*a
    c=0.95*a
    d=a+b+c
    print('gross salary is',d)
else:
    print('enter salary')
