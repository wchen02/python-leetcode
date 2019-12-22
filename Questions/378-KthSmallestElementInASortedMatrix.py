# See details here https://wenshengchen.com/2019/12/15/378-kth-smallest-element-in-a-sorted-matrix.html
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo = matrix[0][0]
        hi = matrix[-1][-1]

        while lo <= hi:
            mid = lo + (hi-lo)//2
            count = 0
            j = len(matrix[0]) - 1

            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > mid: j -= 1
                count += (j + 1)

            if count < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

## TEST CASES
test = Solution()
answer = test.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8)
assert answer == 13, answer
print('All Passed!')