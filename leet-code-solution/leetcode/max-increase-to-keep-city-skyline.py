class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowmaxi=[]
        colmaxi=[]
        ans=0
        maxic=float('-inf')
        for x in grid:
            rowmaxi.append(max(x))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxic=max(maxic,grid[c][r])
            colmaxi.append(maxic)
            maxic=float('-inf')
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans+=min(colmaxi[r],rowmaxi[c])-grid[r][c]



    
        return ans

            

        