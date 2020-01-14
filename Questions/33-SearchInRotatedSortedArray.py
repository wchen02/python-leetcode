from typing import List

# See details here https://wenshengchen.com/2020/01/10/33-search-in-rotated-sorted-array.html
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = lo + (hi-lo) // 2

            if nums[mid] == target:
                return mid
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
            
## TEST CASES
test = Solution()
answer = test.search([4,5,6,7,0,1,2], 0)
assert answer == 4, answer
assert test.search([4,5,6,7,0,1,2], 3) == -1
assert test.search([4,5,6,7,0,1,2], 4) == 0
assert test.search([4,5,6,7,0,1,2], 5) == 1
assert test.search([4,5,6,7,0,1,2], 6) == 2
assert test.search([4,5,6,7,0,1,2], 7) == 3
assert test.search([4,5,6,7,0,1,2], 0) == 4
assert test.search([4,5,6,7,0,1,2], 1) == 5
assert test.search([4,5,6,7,0,1,2], 2) == 6
assert test.search([1,3,5], 1) == 0
assert test.search([1,3,5], 5) == 2
assert test.search([], 3) == -1
print('All Passed!')
