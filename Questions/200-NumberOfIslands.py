from typing import List, Dict

# See details here https://wenshengchen.com/2019/09/04/200-number-of-islands.html
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    numIslands += 1

        return numIslands

    def dfs(self, grid: List[List[str]], row, col) -> None:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] != '1':
            return

        grid[row][col] = '2'
        self.dfs(grid, row-1, col)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row, col+1)

## TEST CASES
test = Solution()
answer = test.numIslands([
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
])
assert answer == 1
answer = test.numIslands([])
assert answer == 0
answer = test.numIslands([
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
])
assert answer == 3
print('All Passed!')
