# See details here https://wenshengchen.com/2019/12/07/53-maximum-subarray.html
import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -sys.maxsize-1
        curSum = -sys.maxsize-1

        for i in range(len(nums)):
            if curSum > 0:
                curSum += nums[i]
            else:
                curSum = nums[i]

            if curSum > maxSum:
                maxSum = curSum

        return maxSum

## TEST CASES
test = Solution()
answer = test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
assert answer == 6
answer = test.maxSubArray([-2])
assert answer == -2
answer = test.maxSubArray([-2,-3])
assert answer == -2
print('All Passed!')
