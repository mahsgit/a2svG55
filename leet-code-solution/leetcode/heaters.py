class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans=0
        houses.sort()
        heaters.sort()

        for val in houses:
            ind=bisect_left(heaters,val)
            cur=abs(val-heaters[ind-1])
            if ind<len(heaters):
                cur=min(cur,heaters[ind]-val)

            ans=max(ans,cur)
                


        return ans


                

                













