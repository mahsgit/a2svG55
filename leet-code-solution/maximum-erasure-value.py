class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:  
        summ=0
        l=0
        maxi=float('-inf')
        check=set()
        for r in range(len(nums)):
            while l<r and nums[r] in check:
                summ-=nums[l]
                check.remove(nums[l])
                l+=1
            check.add(nums[r])
            summ+=nums[r]
            maxi=max(maxi,summ)
        return maxi


   


        