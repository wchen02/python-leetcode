# See details here https://wenshengchen.com/2019/12/13/48-rotate-image.html
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])        
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # reverse each row
        for i in range(n):
            matrix[i].reverse()

## TEST CASES
test = Solution()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
test.rotate(matrix)
assert matrix == [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]
print('All Passed!')