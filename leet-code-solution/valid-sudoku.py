class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)  
        cols = defaultdict(set)  
        grids = defaultdict(set)  
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                elif board[i][j] in cols[j]:
                    return False
                elif board[i][j] in grids[(i//3,j//3)]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grids[(i//3,j//3)].add(board[i][j])
        return True


                

    