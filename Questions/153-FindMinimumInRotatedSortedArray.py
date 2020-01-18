from typing import List

# See details here https://wenshengchen.com/2020/01/17/153-find-minimum-in-rotated-sorted-array.html
class Solution:
    def search(self, nums: List[int]) -> int:
        if not nums: return -1
        
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            if nums[lo] < nums[hi]:
                return nums[lo]

            mid = lo + (hi-lo) // 2

            if nums[0] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]

## TEST CASES
test = Solution()
answer = test.search([4,5,6,7,0,1,2])
assert answer == 0, answer
assert test.search([3,4,5,1,2]) == 1
assert test.search([]) == -1
assert test.search([1]) == 1
assert test.search([1,2]) == 1
assert test.search([2,1]) == 1
assert test.search([1,2,3]) == 1
assert test.search([2,3,1]) == 1
assert test.search([3,1,2]) == 1
assert test.search([1,2,3,4]) == 1
assert test.search([2,3,4,1]) == 1
assert test.search([3,4,1,2]) == 1
assert test.search([4,1,2,3]) == 1
print('All Passed!')
