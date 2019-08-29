from typing import List

# See details here https://wenshengchen.com/2019/08/29/747-largest-numer-at-least-twice-of-others.html
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largestNumIndex = -1
        largestNum = 0
        secondLargestNum = 0
        
        for index, num in enumerate(nums):
            if num >= largestNum:
                secondLargestNum = largestNum
                largestNum = num
                largestNumIndex = index
            elif num > secondLargestNum:
                secondLargestNum = num
        
        if largestNum >= secondLargestNum * 2:
            return largestNumIndex
        
        return -1

## Test Cases
test = Solution()
answer = test.dominantIndex([1,2,3,4])
assert answer == -1
answer = test.dominantIndex([1])
assert answer == 0
answer = test.dominantIndex([1,2])
assert answer == 1
answer = test.dominantIndex([0,99])
assert answer == 1
answer = test.dominantIndex([0,0,3,2])
assert answer == -1
answer = test.dominantIndex([49,99])
assert answer == 1
print('All Passed!')
