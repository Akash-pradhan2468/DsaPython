import logging
logging.basicConfig(level=logging.INFO)# Here we need to set logging level by default wrning in python
# if i write logging.warning("####") then it show by default to show INFO i need to configure


def rotate_by_n(list,n):
    # list=list[-n:]+list[:len(list)-n]
    # It will generate a new variable not change the list itself
    list[:]=list[-n:]+list[:len(list)-n]
    #This will change the variable itself donot create a new variable
    #This take O(N) Tc and O(1) Sc But it is done by only in python 


def rotate_list(list,st,end):
    while st<=end:
        list[st],list[end]=list[end],list[st]
        st+=1
        end-=1

def rotate_list_2(list,n):
    rotate_list(list,0,len(list)-1)
    print(list)
    rotate_list(list,n,len(list)-1) 
    #This mathode takes O(N) Tc and O(1) Sc as it did the task by inplace no extra space is needed

list=[1,2,3,4,5,6,7,8]
# print(list)
logging.info(f"list values are {list}")
rotate_list_2(list,4)
print(list)
# rotate_by_n(list,3)
# print(list)