from typing import List, Dict

# See details here https://wenshengchen.com/2019/09/01/67-add-binary.html
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"

## TEST CASES
test = Solution()
answer = test.addBinary("11", "1")
assert answer == "100"
answer = test.addBinary("1010", "1011")
assert answer == "10101"
answer = test.addBinary("0", "0")
assert answer == "0"
answer = test.addBinary("1111", "1111")
assert answer == "11110"
print('All Passed!')
