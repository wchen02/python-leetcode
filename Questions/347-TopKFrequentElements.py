# See details here https://wenshengchen.com/2019/12/11/347-top-k-frequent-elements.html
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreqMap = {}
        freqNumMap = {}
        topK = []

        for i in nums:
            if i in numFreqMap:
                numFreqMap[i] += 1
            else:
                numFreqMap[i] = 1

        for n, count in numFreqMap.items():
            if count in freqNumMap:
                freqNumMap[count].append(n)
            else:
                freqNumMap[count] = [n]

        for i in range(len(nums), 0, -1):
            countedNums = freqNumMap.get(i)
            if k > 0 and countedNums:
                for j in countedNums:
                    topK.append(j)
                    k -= 1

        return topK

## TEST CASES
test = Solution()
answer = test.topKFrequent([1,1,1,2,2,3],2)
assert answer == [1, 2], answer
answer = test.topKFrequent([1],1)
assert answer == [1], answer
answer = test.topKFrequent([1,1,2,2,3],2)
assert answer == [1, 2], answer
print('All Passed!')