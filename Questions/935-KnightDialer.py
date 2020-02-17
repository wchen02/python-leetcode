from typing import List

# See details here https://wenshengchen.com/2020/02/14/935-knight-dialer.html
class Solution:
    def knightDialer(self, N: int) -> int:
        def moveKnight(i: int, n: int) -> int:
            key = (i,n)
            if key in memo:
                return memo[key]

            if n == 1:
                return 1

            s = 0
            for j in moves[i]:
                s += (moveKnight(j, n-1))
            memo[key] = s
            return memo[key]

        memo = {}
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        modMax = 10**9 + 7
        s = 0
        for i in range(10):
            s += moveKnight(i, N)
        return s % modMax

## TEST CASES
test = Solution()
assert test.knightDialer(1) == 10
assert test.knightDialer(2) == 20
assert test.knightDialer(3) == 46
assert test.knightDialer(50) == 267287516
assert test.knightDialer(5000) == 406880451
print('All Passed!')
