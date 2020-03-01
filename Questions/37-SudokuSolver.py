from typing import List

# See details here https://wenshengchen.com/2020/02/29/37-sudoku-solver.html
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.dfs(board, 0)

    def possibleValues(self, board, col, row):
        valuesSeen = set([])

        for i in range(9):
            if board[row][i] != '.':
                valuesSeen.add(board[row][i])

        for j in range(9):
            if board[j][col] != '.':
                valuesSeen.add(board[j][col])

        x = row // 3
        y = col // 3

        for i in range(x*3, x*3+3):
            for j in range(y*3, y*3+3):
                if board[i][j] != '.':
                    valuesSeen.add(board[i][j])

        return set(['1','2','3','4','5','6','7','8','9']).difference(valuesSeen)

    def dfs(self, board, cellNum):
        row = cellNum // 9
        col = cellNum % 9

        if cellNum >= 81:
            return True

        if board[row][col] != '.':
            if self.dfs(board, cellNum + 1):
                return True
        else:
            values = self.possibleValues(board, col, row)

            original = board[row][col]
            for value in list(values):
                board[row][col] = value
                if self.dfs(board, cellNum + 1):
                    return True
                board[row][col] = original
            return False

## TEST CASES
test = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
test.solveSudoku(board)
assert board == [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
print('All Passed!')
