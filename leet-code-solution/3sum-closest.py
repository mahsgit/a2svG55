class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        big=float('inf')
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                diff=abs(summ-target)
                if diff<big:
                    big=diff
                    value=summ
                if summ>target:
                    r-=1
                elif summ==target:
                    return summ
                else:
                    l+=1
        return value
            
        