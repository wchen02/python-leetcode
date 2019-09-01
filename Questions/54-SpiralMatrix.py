from typing import List

# See details here https://wenshengchen.com/2019/08/31/54-spiral-matrix.html
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        firstRow, firstCol = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        result = []

        while rows > 0 and cols > 0:
            lastRow = firstRow + rows - 1
            lastCol = firstCol + cols - 1

            # Top left to right
            for i in range(cols):
                result.append(matrix[firstRow][firstCol + i])
            # Right top to bottom
            for i in range(1, rows):
                result.append(matrix[firstRow + i][lastCol])
            # Bottom right to left
            for i in range(1, cols):
                if firstRow != lastRow:
                    result.append(matrix[lastRow][lastCol - i])
            # Left bottom to top
            for i in range(1, rows - 1):
                if firstCol != lastCol:
                    result.append(matrix[lastRow - i][firstCol])

            # Next layer
            firstRow += 1
            firstCol += 1
            rows -= 2
            cols -= 2

        return result

## Test Cases
test = Solution()
answer = test.spiralOrder([])
assert answer == [],f"{answer}"
answer = test.spiralOrder([[1]])
assert answer == [1],f"{answer}"
answer = test.spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
assert answer == [1,2,3,6,9,8,7,4,5],f"{answer}"
answer = test.spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
assert answer == [1,2,3,4,8,12,11,10,9,5,6,7],f"{answer}"
answer = test.spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
assert answer == [1,2,3,6,9,12,11,10,7,4,5,8],f"{answer}"
answer = test.spiralOrder([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
])
assert answer == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10],f"{answer}"
answer = test.spiralOrder([[1,2,3,4,5,6,7,8,9,10]])
assert answer == [1,2,3,4,5,6,7,8,9,10]
answer = test.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
assert answer == [1,2,3,4,5,6,7,8,9,10]
print('All Passed!')
