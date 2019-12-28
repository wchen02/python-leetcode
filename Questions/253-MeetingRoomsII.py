from typing import List
import heapq

# See details here https://wenshengchen.com/2019/12/25/253-meeting-rooms-ii.html
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        q = []
        sortedIntervals = sorted(intervals, key = lambda i: i[0])

        for interval in sortedIntervals:
            if q and interval[0] >= q[0]:
                heapq.heappop(q)
            heapq.heappush(q, interval[1])

        return len(q)

## TEST CASES
test = Solution()
assert test.minMeetingRooms([[0, 30],[5, 10],[15, 20]]) == 2
assert test.minMeetingRooms([[7,10],[2,4]]) == 1
assert test.minMeetingRooms([]) == 0
print('All Passed!')
