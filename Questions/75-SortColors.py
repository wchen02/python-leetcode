from typing import List

# See details here https://wenshengchen.com/2019/12/27/75-sort-colors.html
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        redPtr = 0
        bluePtr = len(nums) - 1
        i = 0
        # for i in range(len(nums)):
        while i <= bluePtr:
            if nums[i] == 0:
                nums[i], nums[redPtr] = nums[redPtr], nums[i]
                redPtr += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[bluePtr] = nums[bluePtr], nums[i]
                bluePtr -= 1
            else: 
                i += 1

## TEST CASES
test = Solution()
arr = [2,0,2,1,1,0]
test.sortColors(arr)
assert arr == [0,0,1,1,2,2],arr

arr = [2,0,2,1,1,2]
test.sortColors(arr)
assert arr == [0,1,1,2,2,2]

arr = []
test.sortColors(arr)
assert arr == []

arr = [0]
test.sortColors(arr)
assert arr == [0]

arr = [1]
test.sortColors(arr)
assert arr == [1]

arr = [2]
test.sortColors(arr)
assert arr == [2]

arr = [2,1,0]
test.sortColors(arr)
assert arr == [0,1,2]

arr = [2,0,2,1,1,0,2,1,1,0,2,1,1,0,2,1,1,0,2,1,0,2,1,1,1,0,2,1,1,0,2,1,1,0,2,1,0,2,1,0,2,1,0,2,0,2,1,0,2,1,1,1,1,1,1,1,1,0]
test.sortColors(arr)
assert arr == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
print('All Passed!')
