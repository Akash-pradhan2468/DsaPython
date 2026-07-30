def reverse_array(list,st,end):
    if st>=end:
        return

    # temp=list[st]
    # list[st]=list[end]
    # list[end]=temp
    list[st],list[end]=list[end],list[st]
    # we can swap two number by this mathode as well
    reverse_array(list,st+1,end-1)

list=[1,2,3,4,5,6,7,8]
print(list)
reverse_array(list,0,len(list)-1)
print(list)

# rlist=list[::-1]
# print(rlist)
# This way also we can reverse the array