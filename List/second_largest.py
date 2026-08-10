def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    largest=float("-inf")
    s_largest=float("-inf")
    smallest=float('inf')
    s_smallest=float('inf')

    for i in range(len(a)):
        if a[i]>=largest:
            s_largest=largest
            largest=a[i]
        elif a[i]>s_largest and a[i]!=largest:
            s_largest=a[i]


        
        if a[i]<=smallest:
            s_smallest=smallest
            smallest=a[i]
        elif a[i]<s_smallest and a[i]!=smallest:
            s_smallest=a[i]

            

    return [s_largest,s_smallest]
