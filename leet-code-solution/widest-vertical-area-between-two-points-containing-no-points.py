class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        new=[]
        ans=0
        for i in points:
            new.append(i[0])
        new=sorted(new)
        for i in range(len(new)-1):
            ans=max(new[i+1]-new[i],ans)
        return ans


        