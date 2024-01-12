class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero=0
        l=0
        ans=0
        for r,val in enumerate(nums):
            if val==0:
                zero+=1
                if zero>k:
                    while l<len(nums) and nums[l]!=0:
                        l+=1
                    l+=1
            ans=max(ans,r-l+1)
            print(ans)
        return ans
        
        
        