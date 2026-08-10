

def rotate_by_n(list,n):
    # list=list[-n:]+list[:len(list)-n]
    # It will generate a new variable not change the list itself
    list[:]=list[-n:]+list[:len(list)-n]
    #This will change the variable itself donot create a new variable

list=[1,2,3,4,5,6,8]

rotate_by_n(list,3)
print(list)