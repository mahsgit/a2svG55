class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checker(mid):
            total=0
            for num in nums:
                total+=ceil(num/mid)
            return total





        l=1
        r=max(nums)
        while l<=r:
            mid=(l+r)//2
            val=checker(mid)
            if val>threshold:
                l=mid+1
            else:
                r=mid-1


        return l
        