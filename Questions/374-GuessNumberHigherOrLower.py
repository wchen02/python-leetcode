from typing import List

# See details here https://wenshengchen.com/2020/01/374/374-guess-number-higher-or-lower.html
class Solution:
    def guessNumber(self, n: int) -> int:
        def guess(n: int) -> int:
            # nonlocal guessNum
            if guessNum > n:
                return 1
            elif guessNum < n:
                return -1
            else:
                return 0

        lo, hi = 1, n

        while lo <= hi:
            mid = lo + (hi-lo) // 2

            guessed = guess(mid)
            if guessed < 0:
                hi = mid - 1
            elif guessed > 0:
                lo = mid + 1
            else:
                return mid
        
        return lo

## TEST CASES
test = Solution()
guessNum = 6
assert test.guessNumber(10) == 6
guessNum = 16
assert test.guessNumber(100) == 16
guessNum = 1
assert test.guessNumber(1281) == 1
guessNum = 1281
assert test.guessNumber(1281) == 1281
guessNum = 2
assert test.guessNumber(2) == 2
print('All Passed!')
