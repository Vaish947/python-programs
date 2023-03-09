##########'0'based indexing#########
mylist=[10,20,30,40,50,60,70,80,90]
print(mylist[0])
print(mylist[1])
for i in range(len(mylist)):
    print(mylist[i])
#########'-ve' indexing########
mylist=[10,20,30,40,50,60,70,80,90]
print(mylist[-1])
print(mylist[-2])
##########slicing########
mylist=[10,20,30,40,50,60,70,80,90]
print(mylist[2:7:1])
print(mylist[2:7])
print(mylist[2:])
print(mylist[:7])
print(mylist[::])
print(mylist[::-1])
