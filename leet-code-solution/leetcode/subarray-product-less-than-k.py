class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
         ans=1
         l=r=0
         count=0
         while r<len(nums) :
            ans*=nums[r]
            while l<=r and ans>=k:
                ans//=nums[l]
                l+=1
            if ans < k:
               count+=r-l+1

            r+=1
         return count
        