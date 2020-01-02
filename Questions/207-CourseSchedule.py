from collections import defaultdict
from typing import List

# See details here https://wenshengchen.com/2020/1/1/207-course-schedule.html
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def hasCycle(node):
            if visited[node] == 2:
                return False
            if visited[node] == 1:
                return True
            visited[node] = 1
            if node in nodes:
                for neighbor in nodes[node]:
                    if hasCycle(neighbor):
                        return True
            visited[node] = 2
            return False
        
        nodes = defaultdict(list)
        visited = [0] * numCourses

        for course in prerequisites:
            nodes[course[1]].append(course[0])

        for node in nodes.keys():
            if hasCycle(node):
                return False

        return True

## TEST CASES
test = Solution()
assert test.canFinish(2, [[1,0]]) == True
assert test.canFinish(2, [[1,0],[0,1]]) == False
print('All Passed!')
