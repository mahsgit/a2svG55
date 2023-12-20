class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0

        for col in range(len(strs[0])):
           out=[]

           for row in range(len(strs)):
               out.append(strs[row][col])
            
           if out != sorted(out):
                count+=1
        return count
            


        



        