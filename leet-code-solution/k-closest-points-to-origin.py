class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
     
        points.sort(key=lambda p:sqrt((p[0]**2 )+(p[1]**2)))
        ans=[]
        for i in range(k):
            ans.append(points[i])
        return ans
