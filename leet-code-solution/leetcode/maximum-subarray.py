class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float("-inf")
        curr=0
        n=len(nums)
        l=0
        for r in range(n):
            curr+=nums[r]
            maxi=max(maxi,curr)
            while curr<0:
                curr-=nums[l]
                l+=1
            # maxi=max(maxi,curr)
        return maxi

        