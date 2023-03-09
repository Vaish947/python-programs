mylist=[6,9,1,4,14,2]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
############################
list2=['aaaaaa','bb','ccc']
list2.sort(key=len)
print(list2)
############################
def show(x):
    return x[0]
list3=[[9,2],[4,10]]
print(list3[0])
print(list3[0][1])
print(list3[1],[0])
list3.sort(key=show)
print(list3)
