from typing import List

# See details here https://wenshengchen.com/2020/01/22/416-partition-equal-subset-sum.html
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total//2
        dp = [False]*(target+1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, -1, -1):
                if dp[j] and j+nums[i] <= target:
                    dp[j+nums[i]] = True

        return dp[target]

## TEST CASES
test = Solution()
assert test.canPartition([1, 5, 11, 5]) == True
assert test.canPartition([1, 5, 11, 5, 4]) == False
assert test.canPartition([1, 5, 11, 5, 2]) == True
assert test.canPartition([1, 2, 3, 5]) == False
print('All Passed!')
