#First Way O(n^3)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans_set=set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()
                        ans_set.add(tuple(temp))
        

        return [list(i) for i in ans_set]


#Solution 2 O(n^2)


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans_set=set()
        
        for i in range(0,n):
            demo_set=set()
            for j in range(i+1,n):
                    k=-(nums[i]+nums[j])
                    if k in demo_set:
                        temp=[nums[i],nums[j],k]
                        temp.sort()
                        ans_set.add(tuple(temp))
                    
                    demo_set.add(nums[j])


        return [list(i) for i in ans_set]
    