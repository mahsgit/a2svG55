class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)


        def check(mid):
            count=0
            for val in piles:
                count+=ceil(val/mid)
            return count


        while l<=r:
            mid=(l+r)//2
            k=check(mid)
            if k>h:
                l=mid+1

            else:
                r=mid-1

        return l