class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time=0
        if len(points)==1:
            return total_time
        for i in range(1,len(points)):
            x_difference=abs(points[i][0]-points[i-1][0])
            y_difference=abs(points[i][1]-points[i-1][1])
            if x_difference > y_difference:
                time=x_difference
            else:
                time=y_difference
            total_time+=time
        return total_time


        