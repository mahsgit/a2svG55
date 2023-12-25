class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
    #  maxi=0
    #  add=0
    #  print(len(grid))
    #  for r in range(len(grid)-2):
    #      for c in range(len(grid[0])-1):
    #          add=sum(grid[r][c:c+3]) + grid[r+1][c+1]+sum(grid[r+2][c:c+3])
    #          maxi=max(add,maxi)
    #  return maxi



        res=0
        cur=0
        
        for i in range(len(grid)-2):
            for j in range(1,len(grid[0])-1):
               
                cur=sum(grid[i][j-1:j+2]) +grid[i+1][j] + sum(grid[i+2][j-1:j+2])
                res = max(res,cur)
                                                     
        return res
           

            
            




