class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary=0
        secondary=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-j==0:
                    primary+=mat[i][j]
                elif i+j==len(mat)-1:
                    secondary+=mat[i][j]
        return primary+secondary
                

        