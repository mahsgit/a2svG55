class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        l=-1
        r=len(nums)
        check=set(nums)
        while l+1<r:
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid
        ans[0]=r
        l=-1
        r=len(nums)


        while l+1<r:
            mid=(l+r)//2
            if nums[mid]<=target:
                l=mid

            else:
                r=mid
        ans[1]=l
        if target not in check:
            return [-1,-1]
        else:
           return ans