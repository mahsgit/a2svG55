class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        new=sorted(costs,key=lambda x  : -abs(x[0]-x[1]))
        lena=lenb=len(costs)//2
        total=0
        for a,b in new:
            if lenb==0  or (lena>0 and a<=b) :
                total+=a
                lena-=1
            else:
                total+=b
                lenb-=1

        return total

        