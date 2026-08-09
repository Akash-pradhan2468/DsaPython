def largetst_number(list):
    largest=float('-inf')#list[0] can also take
    for i in range(len(list)):
        largest=max(largest,list[i])
    return largest

list=[-10,5,13,-32,56]
print(largetst_number(list))