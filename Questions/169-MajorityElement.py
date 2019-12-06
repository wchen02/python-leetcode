# See details here https://wenshengchen.com/2019/12/06/169-majority-element.html
from typing import List, Dict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numFreqMap = {}
        maxNum = 0
        maxCount = 0
        
        for i in range(len(nums)):
            if not numFreqMap.get(nums[i]):
                numFreqMap[nums[i]] = 1
            else:
                numFreqMap[nums[i]] += 1

        for k in numFreqMap.keys():
            if numFreqMap.get(k) > maxCount:
                maxNum = k
                maxCount = numFreqMap.get(k)

        return maxNum

## TEST CASES
test = Solution()
answer = test.majorityElement([0,1,0,0,3])
assert answer == 0,answer

answer = test.majorityElement([0,1,0])
assert answer == 0

answer = test.majorityElement([2,2,1,1,1,2,2])
assert answer == 2
print('All Passed!')
