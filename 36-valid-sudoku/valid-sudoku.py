class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row traversal
        n,m=9,9
        for row in range(n):
            sett=set()
            for col in range(m):
                if board[row][col] == ".":
                    continue
                if board[row][col] in sett:
                    return False
                sett.add(board[row][col])
        # col traversal
        for col in range(m):
            sett=set()
            for row in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in sett:
                    return False
                sett.add(board[row][col])
        for sr in range(0, 9, 3):
            for sc in range(0, 9, 3):
                sett = set()
                for i in range(sr, sr + 3):
                    for j in range(sc, sc + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in sett:
                            return False
                        sett.add(board[i][j])
        return True


