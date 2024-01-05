class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length=len(nums)
        ans=set()
        for i in range(length):
            l=i+1
            r=length-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ==0:
                    ans.add((nums[i],nums[l],nums[r]))
                 
                    l+=1
                    r-=1
                elif summ>0:
                    r-=1
                else:
                    l+=1
        return ans


        