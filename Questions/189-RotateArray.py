# See details here https://wenshengchen.com/2019/12/07/189-rotate-array.html
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums or k % len(nums) == 0:
            return

        numsLen = len(nums)
        k = k % numsLen
        curIndex = 0
        curNum = nums[curIndex]

        for _ in range(numsLen):
            nextIndex = (curIndex + k) % numsLen
            nextNum = nums[nextIndex]
            nums[nextIndex] = curNum
            curNum = nextNum
            curIndex = nextIndex
        # nums[k] = curNum

## TEST CASES
test = Solution()
alist = [1,2,3,4,5,6,7]
test.rotate(alist, 3)
assert set(alist) == set([5,6,7,1,2,3,4])

alist = [-1,-100,3,99]
test.rotate(alist, 2)
assert set(alist) == set([3,99,-1,-100]),alist

alist = [1,2]
test.rotate(alist, 3)
assert set(alist) == set([2,1])

alist = [1,2,3,4,5,6]
test.rotate(alist, 3)
assert set(alist) == set([5,6,1,2,3,4]),alist
print('All Passed!')
