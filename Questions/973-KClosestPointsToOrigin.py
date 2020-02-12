import heapq
from typing import List

# See details here https://wenshengchen.com/2020/02/11/973-k-closest-points-to-origin.html
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = [(pt[0]**2 + pt[1]**2, pt) for pt in points]
        pq = heapq.nsmallest(K, distances, key=lambda n: n[0])

        return [item[1] for item in pq]

## TEST CASES
test = Solution()
assert test.kClosest([[1,3],[-2,2]], 1) == [[-2,2]]
assert test.kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3],[-2,4]]
print('All Passed!')
