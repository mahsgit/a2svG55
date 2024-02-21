class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        new=defaultdict(int)
        change=0
        for num in bills:
            if num==10:
                if new[5]<=0:
                    return False
                else:
                    new[5]-=1
            elif num==20:
                if new[10]>0 and new[5]>0:
                     new[10]-=1
                     new[5]-=1
                elif new[5]>=3:
                     new[5]-=3
                else:
                    return False
            new[num]+=1
            

            
        return True

            
        