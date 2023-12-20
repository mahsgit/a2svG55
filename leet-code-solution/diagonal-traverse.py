class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 0,0  0,1   1,0,  2,0  1,1  0,2  1,2  2,1  2,2 
        Map=defaultdict(list)
        flag=False
        out=[]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
               Map[row+col].append(mat[row][col])

        for key ,value in Map.items():
            if flag:
                out+=value
                flag=False
            else:
                out+=value[::-1]
                flag=True
                
        return out






        