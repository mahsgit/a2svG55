class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i=0
        ans=0
        val=1
       
        while val<=n:
            if i<len(nums) and nums[i]<=val:
                val+=nums[i]
                i+=1
            else:
                ans+=1
                val*=2
           
        return ans


        