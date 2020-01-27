from typing import List

# See details here https://wenshengchen.com/2020/01/21/221-maximal-square.html
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maximal = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                maximal = max(maximal, int(matrix[row][col]))

                if row > 0 and col > 0:
                    square = min(int(matrix[row-1][col]), int(matrix[row-1][col-1]), int(matrix[row][col-1]))
                    if square > 0 and matrix[row][col] == "1":
                        matrix[row][col] = str(square + 1)
                        maximal = max(maximal, int(matrix[row][col]))

        return maximal**2

## TEST CASES
test = Solution()
assert test.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
assert test.maximalSquare([["1","0","1","1","1"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 9
assert test.maximalSquare([["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","1","0"]]) == 1
assert test.maximalSquare([["1"]]) == 1
assert test.maximalSquare([[]]) == 0
assert test.maximalSquare(None) == 0
assert test.maximalSquare([["1","1"],["1","1"]]) == 4
print('All Passed!')
