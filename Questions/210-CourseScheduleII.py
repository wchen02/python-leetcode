from collections import defaultdict
from typing import List

# See details here https://wenshengchen.com/2020/01/05/210-course-schedule-ii.html
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def hasCycle(node: int):
            if visited[node] == 2:
                return False
            if visited[node] == 1:
                return True
            
            visited[node] = 1
            for neighbor in nodes[node]:
                if hasCycle(neighbor):
                    return True
            
            visited[node] = 2
            order.append(node)
            return False

        nodes = {}
        for node in range(numCourses):
            nodes[node] = []
        visited = [0] * numCourses
        order = []

        for preq in prerequisites:
            nodes[preq[1]].append(preq[0])

        for node in nodes.keys():
            if visited[node] == 0:
                if hasCycle(node):
                    return []
        
        order.reverse()
        return order if len(order) == numCourses else []

## TEST CASES
test = Solution()
assert test.findOrder(2, [[1,0]]) == [0,1]
answer = test.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
assert answer == [0,1,2,3] or answer == [0,2,1,3], answer
assert test.findOrder(2, [[1,0], [0,1]]) == []
assert test.findOrder(2, [[1,1], [1,1]]) == []
assert test.findOrder(1, []) == [0]
print('All Passed!')
