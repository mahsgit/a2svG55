class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        tar=nums[0]
        if nums[0]==min(nums):
            return nums[0]
        else:
        
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>=tar:

                    l=mid+1
                else:
                    r=mid-1

            return nums[l]


