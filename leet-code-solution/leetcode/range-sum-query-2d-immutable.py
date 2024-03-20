class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rowlen=len(matrix)
        self.collen=len(matrix[0])
        self.new=[[0]* (self.collen+1) for r in range(self.rowlen+1)]

        for r in range(self.rowlen):
            pref=0
            for c in range(self.collen):
                pref+=matrix[r][c]
                above=self.new[r][c+1]
                self.new[r+1][c+1]=pref+above

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2=row1+1,row2+1,col1+1,col2+1
        total=self.new[row2][col2]
        above=self.new[row1-1][col2]
        left=self.new[row2][col1-1]
        topleft=self.new[row1-1][col1-1]
        return total-above-left+topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)