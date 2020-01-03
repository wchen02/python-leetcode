from collections import deque

# See details here https://wenshengchen.com/2020/01/01/277-find-the-celebrity.html
class Solution:
    def findCelebrity(self, n: int) -> int:
        def knows(a: int, b: int) -> bool:
            return graph[a][b]

        candidates = deque([i for i in range(n)])

        while candidates:
            candidate1 = candidates[0]
            candidate2 = candidates[-1]
            
            if candidate1 == candidate2:
                break

            if knows(candidate1, candidate2):
                candidates.popleft()
            else:
                candidates.pop()

        if candidates:
            for i in range(n):
                if i == candidates[0]: continue
                if not knows(i, candidates[0]):
                    return -1
                if knows(candidates[0], i):
                    return -1
            return candidates[0]
        else:
            return -1

## TEST CASES
test = Solution()
graph = [[1,1,0],[0,1,0],[1,1,1]]
assert test.findCelebrity(3) == 1

graph = [[1,0,1],[1,1,0],[0,1,1]]
assert test.findCelebrity(3) == -1

graph = [[1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1],[1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0],[0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0],[1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1],[1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0],[0,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1],[1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1],[0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1],[0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1],[0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1],[1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,1],[1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1],[1,0,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1],[0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1],[0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1],[1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1],[1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0],[0,1,0,0,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,1],[0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1],[1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1],[1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1],[1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1],[0,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1],[0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1],[0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1],[1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1],[1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,1,0,1,1],[1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0],[1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,1],[0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0],[1,0,1,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0],[0,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0],[1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1],[1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0],[1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0],[0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1],[0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0],[1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1],[1,0,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,1],[0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1],[0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,0,1,1,0],[1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,1,1],[0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0],[1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1],[0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1]]
assert test.findCelebrity(51) == 22

graph = [[1,0],[0,1]]
assert test.findCelebrity(2) == -1

graph = [[1,1],[1,1]]
assert test.findCelebrity(2) == -1
print('All Passed!')
