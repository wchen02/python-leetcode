# See details here https://wenshengchen.com/2019/12/08/198-house-robber.html
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        numLength = len(nums)
        if numLength == 0:
            return 0
        elif numLength == 1:
            return nums[0]
        elif numLength == 2:
            return max(nums[0], nums[1])

        nums[2] = nums[2] + nums[0]
        
        for i in range(3,numLength):
            nums[i] = nums[i] + max(nums[i-2], nums[i-3])

        return max(nums[numLength-2], nums[numLength-1])

## TEST CASES
test = Solution()
answer = test.rob([1,2,3,1])
assert answer == 4

answer = test.rob([2,7,9,3,1])
assert answer == 12

answer = test.rob([])
assert answer == 0

answer = test.rob([3,2,3,4])
assert answer == 7
print('All Passed!')
