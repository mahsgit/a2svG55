class Solution:
    def minimumSteps(self, s: str) -> int:
        val=list(map(int,s))
        l=0
        r=len(s)-1
        count=0
        while l<r:
            if val[l]==1:
                while r>l and val[r]==1:
                    r-=1
                val[l],val[r]=val[r],val[l]
                count+=r-l

                r-=1
            l+=1
        return count
            

        