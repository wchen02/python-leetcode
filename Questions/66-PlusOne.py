from typing import List

# See details here # See details here https://wenshengchen.com/2019/08/29/66-plus-one.html
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if (digits[i] < 9):
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        digits[0] = 1
        digits.append(0)
        return digits

## Test Cases
test = Solution()
answer = test.plusOne([0])
assert answer == [1]
answer = test.plusOne([9])
assert answer == [1,0]
answer = test.plusOne([9,9])
assert answer == [1,0,0]
answer = test.plusOne([9,9,1])
assert answer == [9,9,2]
answer = test.plusOne([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9])
assert answer == [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print('All Passed!')