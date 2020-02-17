from collections import defaultdict
from typing import List

# See details here https://wenshengchen.com/2020/02/14/364-nested-list-weight-sum-ii.html
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def getNestedList(nestedList: List[NestedInteger], depth: int) -> None:
            maxDepth = max(maxDepth, depth)
            
            for n in nestedList:
                if n.isInteger():
                    hashmap[depth] += n.getInteger()
                else:
                    getNestedList(n.getList(), depth+1)

        hashmap = defaultdict(int)
        maxDepth = 0
        getNestedList(nestedList, 0)

        sum = 0
        for i in range(maxDepth):
            sum += hashmap[i] * (maxDepth - i)

        return sum


## TEST CASES
test = Solution()
assert test.knightDialer(1) == 10
print('All Passed!')
