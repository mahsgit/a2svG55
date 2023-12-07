class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # ans=0
        # if start>destination:
        #     start,destination=destination,start

        # for i in range(len(distance)):
        #     if destination == i:
        #         if sum(distance[start:i])<(sum(distance[i:])+sum(distance[0:start])):
        #             ans=sum(distance[start:i])
        #             break
        #         else:
        #             ans=sum(distance[i:])+sum(distance[0:start])
        #             break
                    
            
                
        # return ans 
        if start > destination:
            start, destination = destination , start
        clockwiseDis = sum(distance[start:destination])
        return min(clockwiseDis, sum(distance) - clockwiseDis)


     
