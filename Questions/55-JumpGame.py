from typing import List

# See details here https://wenshengchen.com/2020/01/12/55-jump-game.html
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return True
        
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            if dp[i-1]-1 < 0:
                return False
            
            dp[i] = max(dp[i-1]-1, nums[i])
            
        return dp[len(nums)-1] >= 0

## TEST CASES
test = Solution()
assert test.canJump([2,3,1,1,4]) == True
assert test.canJump([3,2,1,0,4]) == False
assert test.canJump([]) == True
print('All Passed!')