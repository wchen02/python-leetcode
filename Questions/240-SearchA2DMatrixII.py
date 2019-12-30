from typing import List

# See details here https://wenshengchen.com/2019/12/29/240-search-a-2-d-matrix-ii.html
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def getSmallestNumLargerThanK(arr: List[int]):
            lo = 0
            hi = len(arr)

            while lo < hi:
                mid = lo + (hi-lo)//2

                if arr[mid] > target:
                    hi = mid
                else:
                    lo = mid+1

            return lo

        if not matrix or not matrix[0]:
            return False

        col = getSmallestNumLargerThanK(matrix[0])
        row = getSmallestNumLargerThanK([matrix[i][0] for i in range(len(matrix))])

        for i in range(row):
            n = getSmallestNumLargerThanK(matrix[i][:col])
            if matrix[i][n-1] == target:
                return True

        return False

## TEST CASES
test = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
assert test.searchMatrix([], 5) == False
assert test.searchMatrix([[]], 5) == False
assert test.searchMatrix(matrix, 5) == True
assert test.searchMatrix(matrix, 20) == False
assert test.searchMatrix(matrix, 21) == True
assert test.searchMatrix(matrix, 22) == True
assert test.searchMatrix(matrix, 23) == True
assert test.searchMatrix(matrix, 10) == True
assert test.searchMatrix(matrix, 25) == False
assert test.searchMatrix(matrix, 27) == False
print('All Passed!')
