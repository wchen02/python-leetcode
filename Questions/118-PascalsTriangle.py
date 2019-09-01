from typing import List

# See details here https://wenshengchen.com/2019/08/31/118-pascals-triangle.html
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            newList = [1] * (i+1)
            for j in range(1, len(newList) - 1):
                newList[j] = result[i-1][j-1] + result[i-1][j]
            result.append(newList)

        return result

## Test Cases
test = Solution()
answer = test.generate(0)
assert answer == []
answer = test.generate(1)
assert answer == [[1]]
answer = test.generate(2)
assert answer == [[1],[1,1]]
answer = test.generate(5)
assert answer == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print('All Passed!')
