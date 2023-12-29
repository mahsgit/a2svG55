class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
       
        count=0
        other=0
        for i ,value in enumerate(flips,1):
            other=max(value,other)
            if other==i:
                count+=1
        return count


    
        