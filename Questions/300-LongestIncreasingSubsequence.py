from typing import List

# See details here https://wenshengchen.com/2019/12/29/300-longest-increasing-subsequence.html
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif sub[mid] > val:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)

## TEST CASES
test = Solution()
assert test.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
assert test.lengthOfLIS([1,9,2,5,3,7,101,18]) == 5
assert test.lengthOfLIS([]) == 0
assert test.lengthOfLIS([1]) == 1
assert test.lengthOfLIS([4,3,2,1]) == 1
assert test.lengthOfLIS([4,10,4,3,8,9]) == 3
assert test.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]) == 6
print('All Passed!')
