a=int(input('enter marks of physics'))
b=int(input('enter marks of chemistry'))
c=int(input('enter marks of biology'))
d=int(input('enter marks of mathematics'))
e=int(input('enter marks of computer'))
f=(a+b+c+d+e)/5
if f>=90:
    print('percentage is',f,'grade is A',)
elif f>=80:
    print('percentage is',f,'grade is B')
elif f>=70:
    print('percentage is',f,'grade is C')
elif f>=60:
    print('percentage is',f,'grade is D')
elif f>=40:
    print('percentage is',f,'grade is E')
elif f<40:
    print('percentage is',f,'grade is F')
else:
    print('fail')
