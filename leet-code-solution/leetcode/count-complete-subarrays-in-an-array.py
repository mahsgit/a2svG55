class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        real=set(nums)
        check=set()
        count=0
        for i in range(len(nums)):
            check.add(nums[i])
            if len(check)==len(real):
                    count+=1
            for j in range(i+1,len(nums)):
                check.add(nums[j])
                if len(check)==len(real):
                    count+=1

            check=set()
        return count