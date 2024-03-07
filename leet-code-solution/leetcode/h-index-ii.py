class Solution:
    def hIndex(self, citations: List[int]) -> int:

        l=0
        r=citations[-1]
        def check(mid):
            
            return len(citations)-bisect_left(citations,mid)>=mid




        while l<=r:
            mid=(l+r)//2
          
            if check(mid):
                l=mid+1

            else:
                r=mid-1

        return r

       
