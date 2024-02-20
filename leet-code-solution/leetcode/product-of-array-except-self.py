class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        multi=1
        ans=[0]*len(nums)
        for val in nums:
            multi*=val

        if count[0]==1:
            valu=1
            for val in nums:
                if val ==0:
                    continue
                valu*=val
            zero=nums.index(0)
            ans[zero]=valu
            return ans

        elif count[0] >1:
            return ans

        elif count[0]==0:
            for i in range(len(nums)):
                ans[i]=multi//nums[i]
            return ans

