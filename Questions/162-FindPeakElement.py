from typing import List
import sys

# See details here https://wenshengchen.com/2019/12/29/162-find-peak-element.html
class Solution:
    def findPeakElement2(self, nums: List[int]) -> int:
        if not nums:
            return -1

        lo, hi = 0, len(nums)-1
        
        while lo+1 < hi:
            mid = lo + (hi-lo)//2
            left = nums[mid-1]
            right = nums[mid+1]
            
            if left < nums[mid] and nums[mid] > right:
                return mid
            elif left < nums[mid] and nums[mid] < right:
                lo = mid
            else:
                hi = mid
        

        for i in [lo, hi]:
            left = nums[i-1] if i - 1 >= 0 else -sys.maxsize-1
            right = nums[i+1] if i + 1 < len(nums) else -sys.maxsize-1
            if left < nums[i] and nums[i] > right:
                return i

        return -1

    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return -1
        if len(nums) == 1: return 0

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid1 = lo + (hi-lo)//2
            mid2 = mid1 + 1

            if nums[mid1] < nums[mid2]:
                lo = mid1 + 1
            else:
                hi = mid1

        return lo

## TEST CASES
test = Solution()
answer = test.findPeakElement([1,2,3,1])
assert answer == 2, answer

answer = test.findPeakElement([1,2,3,4])
assert answer == 3, answer

answer = test.findPeakElement([8,7,6,5])
assert answer == 0, answer

answer = test.findPeakElement([9])
assert answer == 0, answer

answer = test.findPeakElement([])
assert answer == -1, answer

answer = test.findPeakElement([1,2,1,3,5,6,4])
assert answer == 1 or answer == 5, answer
print('All Passed!')
