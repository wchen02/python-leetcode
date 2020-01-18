from typing import List

# See details here https://wenshengchen.com/2020/01/16/278-first-bad-version.html
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def isBadVersion(version: int) -> bool:
            return version >= firstBad

        if n == 1: return 1

        lo, hi = 1, n

        while lo < hi:
            mid1 = lo + (hi-lo) // 2
            mid2 = mid1 + 1

            isMid1Bad = isBadVersion(mid1)
            isMid2Bad = isBadVersion(mid2)
            
            if not isMid1Bad and isMid2Bad:
                return mid2
            elif not isMid1Bad:
                lo = mid1 + 1
            else:
                hi = mid1

        return lo

## TEST CASES
test = Solution()
firstBad = 4
assert test.firstBadVersion(5) == 4
firstBad = 3
assert test.firstBadVersion(10) == 3
firstBad = 1
assert test.firstBadVersion(1) == 1
firstBad = 10
assert test.firstBadVersion(10) == 10
firstBad = 1
assert test.firstBadVersion(4) == 1
firstBad = 2
assert test.firstBadVersion(4) == 2
firstBad = 3
assert test.firstBadVersion(4) == 3
firstBad = 4
assert test.firstBadVersion(4) == 4
print('All Passed!')
