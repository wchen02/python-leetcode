from typing import List

# See details here https://wenshengchen.com/2020/01/14/69-sqrt-x.html
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x

        while lo <= hi:
            mid = lo + (hi-lo)//2

            square = mid**2
            if square == x:
                return mid
            elif square < x:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return hi

## TEST CASES
test = Solution()
assert test.mySqrt(0) == 0
assert test.mySqrt(1) == 1
assert test.mySqrt(4) == 2
assert test.mySqrt(8) == 2
assert test.mySqrt(11) == 3
print('All Passed!')
