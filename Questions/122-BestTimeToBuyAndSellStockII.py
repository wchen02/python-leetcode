# See details here https://wenshengchen.com/2019/12/04/122-best-time-to-buy-and-sell-stock-ii.html
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

## TEST CASES
test = Solution()
answer = test.maxProfit([7,1,5,3,6,4])
assert answer == 7

answer = test.maxProfit([1,2,3,4,5])
assert answer == 4
print('All Passed!')
