# See details here https://wenshengchen.com/2019/12/16/215-kth-largest-element-in-an-array.html
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]
        hq = []
        for n in nums:
            if len(hq) < k:
                heapq.heappush(hq, n)
            else:
                heapq.heappushpop(hq, n)
        return heapq.heappop(hq)

## TEST CASES
test = Solution()
answer = test.findKthLargest([3,2,1,5,6,4], 2)
assert answer == 5, answer
answer = test.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
assert answer == 4, answer
print('All Passed!')