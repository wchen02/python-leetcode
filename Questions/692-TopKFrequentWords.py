import heapq
from collections import Counter
from typing import List

# See details here https://wenshengchen.com/2020/01/24/692-top-k-frequent-words.html
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = Counter(words)
        pq = heapq.nsmallest(k, hashmap.items(), lambda n: (-n[1], n[0]))
        
        return map(lambda n: n[0], pq)

## TEST CASES
test = Solution()
assert test.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
assert test.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
print('All Passed!')
