from typing import List

# See details here https://wenshengchen.com/2019/12/30/73-set-matrix-zeroes.html
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        isRowZero, isColZero = False, False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if matrix[row][0] == 0:
                        isRowZero = True
                    if matrix[0][col] == 0:
                        isColZero = True
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if isRowZero:
            for row in range(rows):
                matrix[row][0] = 0

        if isColZero:
            for col in range(cols):
                matrix[0][col] = 0

## TEST CASES
test = Solution()
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
test.setZeroes(matrix)
assert matrix == [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
test.setZeroes(matrix)
assert matrix == [
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

matrix = []
test.setZeroes(matrix)
assert matrix == []

matrix = [[]]
test.setZeroes(matrix)
assert matrix == [[]]
print('All Passed!')
