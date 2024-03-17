class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums=nums[::-1]
        print(nums)
        mini=nums[0]
        ans=0
        for i in range(1,len(nums)):
            if nums[i]>mini:
                if nums[i]%mini:
                    count=nums[i]//mini+1
                    mini=nums[i]//count
                else:
                    count=nums[i]//mini
                ans+=count-1
            else:
                mini=nums[i]
                 
                
        return ans
            