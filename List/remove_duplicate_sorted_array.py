def remove_duplicate(list):
    i=1
    for k in range(1,len(list)):
        if list[k]!=list[k-1]:
            list[i]=list[k]
            i+=1


list=[1,2,3,3,4,4,5,6,6]
remove_duplicate(list)
print(list)
