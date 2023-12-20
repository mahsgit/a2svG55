class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=[]


        for i in range(len(matrix[0])):
            col=[]

            for j in range(len(matrix)):
                 col.append(matrix[j][i])
            row.append(col)



        return row