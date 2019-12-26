# See details here https://wenshengchen.com/2019/12/07/189-rotate-array.html
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        count = 0

        for i in range(n):
            if count >= n:
                break
            curI = i
            prev = nums[i]

            nextI = (curI + k) % n
            temp = nums[nextI]
            nums[nextI] = prev
            prev = temp

            curI = nextI
            count += 1
            
            while (curI != i):
                nextI = (curI + k) % n
                temp = nums[nextI]
                nums[nextI] = prev
                prev = temp
                curI = nextI
                count += 1

## TEST CASES
test = Solution()
alist = [1,2,3,4,5,6,7]
test.rotate(alist, 3)
assert set(alist) == set([5,6,7,1,2,3,4]),alist

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
