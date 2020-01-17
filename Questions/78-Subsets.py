# See details here https://wenshengchen.com/2019/12/05/78-subsets.html
from typing import List, Dict

class Solution:
    def subsetsHelper(self, nums: List[int], result: List[List[int]], arr: List[int], i: int) -> None:
        result.append(arr.copy())

        for j in range(i, len(nums)):
            arr.append(nums[j])
            self.subsetsHelper(nums, result, arr, j+1)
            arr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subsetsHelper(nums, result, [], 0)
        return result

## TEST CASES
test = Solution()
answer = test.subsets([1,2,3])
answer = list(answer)
answer.sort()
assert answer == [
    [],
    [1],
    [1,2],
    [1,2,3],
    [1,3],
    [2],
    [2,3],
    [3],
], answer
print('All Passed!')