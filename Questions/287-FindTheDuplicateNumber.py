# See details here https://wenshengchen.com/2019/12/14/287-find-the-duplicate-number.html
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

## TEST CASES
test = Solution()
assert test.findDuplicate([1,3,4,2,2]) == 2
assert test.findDuplicate([3,1,3,4,2]) == 3
print('All Passed!')