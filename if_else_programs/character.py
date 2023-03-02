a=(input('enter any character'))
b=ord(a)
if b>=65 and b<=90:
    print('it is a capital letter')
elif b>=97 and b<=122:
    print('it is a small letter')
else:
    print('it is a special character')
############################################
a=input('enter any character')
b=ord(a)
if b>=65 and b<=122:
    print('it is an alphabet')
else:
    print('it is not an alphabet')