class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        length=len(nums)
        ans=0
        for r in range(length):
            k-=1-nums[r]
            while k<0:
                k+=1-nums[l]
                l+=1
            
            ans=max(ans,r-l+1)
        return ans
        