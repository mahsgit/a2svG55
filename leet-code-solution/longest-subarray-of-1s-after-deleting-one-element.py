class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero=0
        l=r=ans=0
        while r<len(nums):
            if nums[r]==0:
                zero+=1
            
            if zero>1:
                while nums[l]!=0:
                    l+=1
                zero=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans-1
        
        