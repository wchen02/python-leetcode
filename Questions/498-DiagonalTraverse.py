from typing import List

# See details here # See details here https://wenshengchen.com/2019/08/30/498-diagonal-traverse.html
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        
        # Row and Col Directions
        directions = [
            [-1, 1],
            [1, -1],
        ]

        # Index to directions
        curDir = 0
        curRow = 0
        curCol = 0
        numRows = len(matrix)
        numCols = len(matrix[0])

        for i in range(numRows * numCols):
            result.append(matrix[curRow][curCol])

            # Top right corner
            if curRow + directions[curDir][0] < 0 and curCol + directions[curDir][1] == numCols:
                curRow += 1
                curDir = (curDir + 1) % 2
            # Bottom left corner
            elif curCol + directions[curDir][1] < 0 and curRow + directions[curDir][0] == numRows:
                curCol += 1
                curDir = (curDir + 1) % 2
            # Left or right edge
            elif curCol + directions[curDir][1] == numCols or curCol + directions[curDir][1] < 0:
                curRow += 1
                curDir = (curDir + 1) % 2
            # Top or bottom edge
            elif curRow + directions[curDir][0] == numRows or curRow + directions[curDir][0] < 0:
                curCol += 1
                curDir = (curDir + 1) % 2
            else:
                curRow += directions[curDir][0]
                curCol += directions[curDir][1]

        return result

## Test Cases
test = Solution()
answer = test.findDiagonalOrder([])
assert answer == []
answer = test.findDiagonalOrder([[0]])
assert answer == [0]
answer = test.findDiagonalOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9],
])
assert answer == [1,2,4,7,5,3,6,8,9]
answer = test.findDiagonalOrder([
    [1,2,3],
    [4,5,6],
])
assert answer == [1,2,4,5,3,6]
answer = test.findDiagonalOrder([
    [1,2,3],
])
assert answer == [1,2,3]
answer = test.findDiagonalOrder([
    [1,2],
    [4,5],
    [7,8],
])
assert answer == [1,2,4,7,5,8]
answer = test.findDiagonalOrder([
    [1],
    [4],
    [7],
])
assert answer == [1,4,7]
print('All Passed!')