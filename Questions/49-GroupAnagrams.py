# See details here https://wenshengchen.com/2019/12/17/49-group-anagrams.html
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for aStr in strs:
            hashmap[str(sorted(aStr))].append(aStr)

        return list(hashmap.values())

## TEST CASES
test = Solution()
answer = test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
assert answer == [
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
], answer
print('All Passed!')