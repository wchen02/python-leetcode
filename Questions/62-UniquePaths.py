# See details here https://wenshengchen.com/2019/12/19/62-unique-paths.html
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1

        path = [[1 for i in range(m)] for j in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                path[i][j] = path[i+1][j] + path[i][j+1]
        return path[0][0]

## TEST CASES
test = Solution()
assert test.uniquePaths(3, 2) == 3
assert test.uniquePaths(7, 3) == 28
print('All Passed!')