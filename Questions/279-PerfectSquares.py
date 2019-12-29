from typing import List
import math
import sys

# See details here https://wenshengchen.com/2019/12/28/279-perfect-squares.html
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [sys.maxsize] * (n+1)

        for i in range(1, n+1):
            if i in squares:
                dp[i] = 1
            else:
                ps = math.floor(math.sqrt(i))
                for j in range(ps, 0, -1):
                    dp[i] = min(dp[i], 1 + dp[i - squares[j]])
        return dp[n]

## TEST CASES
test = Solution()
answer = test.numSquares(12)
assert answer == 3, answer
assert test.numSquares(13) == 2
assert test.numSquares(1001) == 3
print('All Passed!')
