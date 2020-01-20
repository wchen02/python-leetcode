from typing import List

# See details here https://wenshengchen.com/2020/01/19/39-combination-sum.html
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(combo: List[int], i: int, sum: int) -> None:
            if sum > target:
                return

            if sum == target:
                combos.append(combo.copy())
                return

            for c in range(i, len(candidates)):
                dfs(combo + [candidates[c]], c, sum + candidates[c])

            return

        if not candidates: return []
        combos = []
        dfs([], 0, 0)
        return combos

## TEST CASES
test = Solution()
answer = test.combinationSum([2,3,6,7], 7)
assert answer == [
  [2,2,3],
  [7]
], answer
answer = test.combinationSum([2,3,5], 8)
assert answer == [
  [2,2,2,2],
  [2,3,3],
  [3,5]
], answer
print('All Passed!')
