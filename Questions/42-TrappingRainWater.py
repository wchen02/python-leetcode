from typing import Dict, List
from collections import defaultdict, deque

# See details here https://wenshengchen.com/2020/02/26/42-trapping-rain-water.html
class Solution:
    def trap(self, height: List[int]) -> int:
        rightMax = []
        
        currMax = 0
        for i in range(len(height)-1, -1, -1):
            currMax = max(currMax, height[i])
            rightMax.append(currMax)
            
        leftMax = 0
        trapped = 0
        for i in range(len(height)):
            leftMax = max(leftMax, height[i])
            minHeight = min(leftMax, rightMax[len(height) - 1 - i])
            trapped += minHeight - height[i]

        return trapped

## TEST CASES
test = Solution()
assert test.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
print('All Passed!')
