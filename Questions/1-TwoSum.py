from typing import List, Dict

# See details here https://wenshengchen.com/2019/08/27/1-two-sum.html
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict: Dict[int, int] = {}

        for idx, num in enumerate(nums):
            dict[num] = idx
        for idx, num in enumerate(nums):
            idx2 = dict.get(target - num)
            if idx2 != idx and idx2 != None:
                return [idx, idx2]

        return []

## TEST CASES
test = Solution()
answer = test.twoSum([1,2,3,4], 6)
assert answer == [1,3]
answer = test.twoSum([1,7,3,3,4], 6)
assert answer == [2,3]
answer = test.twoSum([1,5], 6)
assert answer == [0,1]
answer = test.twoSum([-2**31,700, 1, 5, 45467, 94351231, 2**31-1, 456123197], -1)
assert answer == [0,6]
answer = test.twoSum([3,2,4], 6)
assert answer == [1,2]
print('All Passed!')
