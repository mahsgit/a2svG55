class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n=len(nums)
        r=len(nums)-1
        nums.sort()
        l=0
        ans=0
        modu=10**9+7
        while l<=r:
            if nums[l]+nums[r]>target:
                r-=1

            else:
                ans+=(2**(r-l)) % modu
                l+=1

        return ans % modu


        # total number of subsequences
        # total number of subarray




        