class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      
        # ranges.sort()
        # last = sorted(ranges, key=lambda j: j[1])
        # new = list(range(left, right + 1))
        # oring = list(range(ranges[0][0], last[-1][1] + 1))
        
        # if all(i in oring for i in new):
        #     return True
        
        # return False
       
        for i in range(left, right + 1):
            for l, r in ranges:
                if l <= i <= r:
                    break
            else:
                return False
                
        return True

