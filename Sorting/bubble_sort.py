def bubble_sort(list):
    n=len(list)
    flag=True
    for i in range(n-2,-1,-1):
        for j in range(0,i+1,1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                flag=False

        if flag==True:
            break

list=[1,2,3,4,5,6]
bubble_sort(list)
print(list)