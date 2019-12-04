from typing import List

# See details here https://wenshengchen.com/2019/12/04/344-reverse-string.html
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(int(len(s) / 2)):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp

## TEST CASES
test = Solution()
testStr = ['a', 'b', 'c']
test.reverseString(testStr)
assert testStr == ['c', 'b', 'a']

testStr = []
test.reverseString(testStr)
assert testStr == []

testStr = ['a']
test.reverseString(testStr)
assert testStr == ['a']
print('All Passed!')
