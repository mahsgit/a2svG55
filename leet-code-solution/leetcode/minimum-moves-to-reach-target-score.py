class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total=0
        while target>1 and maxDoubles>0:
            if target%2==0  :
                total+=1
                maxDoubles-=1
                target//=2
            else:
                total+=1
                target-=1

        return total-1+target
        

        