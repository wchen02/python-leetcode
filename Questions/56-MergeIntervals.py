from typing import List

# See details here https://wenshengchen.com/2020/01/03/56-merge-intervals.html
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key = lambda n: n[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        
        return result

## TEST CASES
test = Solution()
assert test.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert test.merge([[1,4],[4,5]]) == [[1,5]]
assert test.merge([]) == []
print('All Passed!')
