import random
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

print(f"n={n}\nm={m}\nfrequency values of m in n are\n{return_count_function(n,m)} ")