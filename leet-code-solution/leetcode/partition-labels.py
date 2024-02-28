class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=0
        r=0
        z=0
        ans=[]
        for val in s:
            if s.rindex(val) >r:
               r=s.rindex(val)
            if l==r:
                ans.append(r+1-z)
                z=r+1
            l+=1
                

        return ans
