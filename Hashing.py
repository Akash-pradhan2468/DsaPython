import random
import string

# RANDOM NUMBER AND HASHING ON NUMBER


length=random.randint(1,20)
n=[random.randint(1,100) for i in range(length)]
m=[random.randint(1,100) for i in range(length)]
print(n)
print(m)

def return_count_function(list1,list2):
    freq={}
    for i in list1:
        freq[i]=freq.get(i,0)+1

    ans_freq={}
    for i in list2:
        for i in list2:
            ans_freq[i]=freq.get(i,0)

    return ans_freq

# print(f"n={n}\nm={m}\nfrequency values of m in n are\n{return_count_function(n,m)} ")


# RANDOM STRING AND HASHING 

str_length=random.randint(1,10)
str1="".join(random.choices(string.ascii_letters,k=str_length))
list_str=[random.choice(string.ascii_letters) for i in range(random.randint(1,10))]

def str_frequency(str3,str_list):
    dict={}
    for i in str3:
        dict[i]=dict.get(i,0)+1

    ans_str_freq={}

    for i in str_list:
        ans_str_freq[i]=dict.get(i,0)

    return ans_str_freq

print(f"String={str1}\nstring_list={list_str}\nfrequency of the string in the list in string are\n{str_frequency(str1,list_str)}")




