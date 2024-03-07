from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        if n != m:
            return False

        cubic_set = [set() for i in range(n)]
        row_set = [set() for i in range(n)]
        col_set = [set() for i in range(n)]

        count = 0
        for i in range(n):
            for j in range(m):
                count += 1
                if board[i][j] == '.' :
                    pass
                elif board[i][j] not in row_set[i]:
                    row_set[i].add(board[i][j])
                else:
                    return False

                if board[j][i] == '.':
                    pass
                elif board[j][i] not in col_set[i]:
                    col_set[i].add(board[j][i])
                else:
                    return False

                if board[i][j] == '.' :
                    pass
                elif board[i][j] not in cubic_set[i // 3 * 3 + j //3]:
                    cubic_set[i // 3 * 3 + j // 3].add(board[i][j])
                else:
                    return False

        return True


if __name__ == "__main__":
    solution = Solution()
    board = [
          ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert solution.isValidSudoku(board)

    board = [
         ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert solution.isValidSudoku(board) == False
