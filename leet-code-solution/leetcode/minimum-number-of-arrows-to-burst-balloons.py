class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count=1
        points.sort()
        print(points)
        prev=points[0][1]
        for i in range(1,len(points)):
            if prev>=points[i][0]:
                prev=min(prev,points[i][1])
            else:
                count+=1
                prev=points[i][1]
        return count

       

        