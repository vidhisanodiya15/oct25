mylist=[1,2,2,3,3,4,5,5,5,6,6]
new_list=[]
for num in mylist:
    if mylist.count(num)==1:
        new_list.append(num)
print(new_list)

