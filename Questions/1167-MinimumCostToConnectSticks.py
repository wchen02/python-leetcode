import heapq
from typing import List

# See details here https://wenshengchen.com/2020/02/11/1167-minimum-cost-to-connect-sticks.html
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minimum = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            newVal = heapq.heappop(sticks)+heapq.heappop(sticks)
            minimum += newVal
            heapq.heappush(sticks, newVal)
        return minimum

## TEST CASES
test = Solution()
assert test.connectSticks([2,4,3]) == 14
assert test.connectSticks([1,8,3,5]) == 30
assert test.connectSticks([1]) == 0
print('All Passed!')
