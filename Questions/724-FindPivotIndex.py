from typing import List

# See details here https://wenshengchen.com/2019/08/28/724-find-pivot-index.html
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        for idx, num in enumerate(nums):
            leftSum += num
            if leftSum == rightSum:
                return idx
            rightSum -= num

        return -1

## Test Cases
test = Solution()
answer = test.pivotIndex([1,2,3,4,6])
assert answer == 3
answer = test.pivotIndex([-1,1,-2,2,3,4,-4])
assert answer == 4
answer = test.pivotIndex([-1,1,-2,2,-3,3,4,-4])
assert answer == -1
answer = test.pivotIndex([-1,-1,0,0,-1,-1])
assert answer == 2
answer = test.pivotIndex([1,2,1])
assert answer == 1
answer = test.pivotIndex([1,2])
assert answer == -1
answer = test.pivotIndex([1])
assert answer == 0
answer = test.pivotIndex([])
assert answer == -1
print('All Passed!')
