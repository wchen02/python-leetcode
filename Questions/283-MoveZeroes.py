# See details here https://wenshengchen.com/2019/12/06/283-move-zeroes.html
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroIndex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroIndex] = nums[i]
                nonZeroIndex += 1

        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0

## TEST CASES
test = Solution()
numList = [0,1,0,2,3]
test.moveZeroes(numList)
assert numList == [1,2,3,0,0], numList

numList = [0,1]
test.moveZeroes(numList)
assert numList == [1,0], numList

numList = [1,2,3,0,0]
test.moveZeroes(numList)
assert numList == [1,2,3,0,0], numList

numList = [1,2,3]
test.moveZeroes(numList)
assert numList == [1,2,3], numList
print('All Passed!')
