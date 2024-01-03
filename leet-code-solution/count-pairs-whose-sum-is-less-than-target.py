class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        count=0
        print(nums)
        # for i in range(len(nums)):
        #     j=i+1
        #     while j<len(nums) and nums[i]+nums[j]<target:
        #         count+=1
        #         j+=1
        # return count
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]+nums[r]>=target:
                r-=1
            else:
                count+=r-l
                l+=1
        return count
       



            
        