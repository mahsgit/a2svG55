class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        mido=0

        def check(mid):
            temp=0
            count=0
            for val in weights:
                if temp+val<=mid:
                   temp+=val
                else:
                    count+=1
                    temp=0
                    temp+=val
            
            return count+1


        while l<=r:
            mid=(r+l)//2
            if check(mid)<=days:
                mido=mid
                r=mid-1

            else:
                l=mid+1
        return mido


        