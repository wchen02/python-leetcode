from typing import List
# See details here https://wenshengchen.com/2019/12/20/11-container-with-most-water.html
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            area = (right-left) * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

## TEST CASES
test = Solution()
assert test.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert test.maxArea([1,2]) == 1
assert test.maxArea([2,3,4,5,18,17,6]) == 17
print('All Passed!')