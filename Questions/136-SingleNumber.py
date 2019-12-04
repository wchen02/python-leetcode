from typing import List

# See details here https://wenshengchen.com/2019/12/04/136-single-number.html
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums)):
            result ^= nums[i]

        return result

## TEST CASES
test = Solution()
answer = test.singleNumber([1,1,2,4,2,3,3])
assert answer == 4

answer = test.singleNumber([1])
assert answer == 1
print('All Passed!')
