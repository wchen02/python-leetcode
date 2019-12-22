# See details here https://wenshengchen.com/2019/12/04/22-generate-parentheses.html
from typing import List

class Solution:
    def generateParenthesisHelper(self, parenthesis: [str], curStr: str, openParens: int, closeParens: int) -> None:
        if openParens == 0 and closeParens == 0:
            parenthesis.append(curStr)
            return

        if openParens > 0:
            self.generateParenthesisHelper(parenthesis, curStr + '(', openParens-1, closeParens)
        
        if closeParens > openParens:
            self.generateParenthesisHelper(parenthesis, curStr + ')', openParens, closeParens-1)

    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []
        self.generateParenthesisHelper(parenthesis, "", n, n)
        return parenthesis

## TEST CASES
test = Solution()
answer = test.generateParenthesis(3)
assert answer == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
], answer
print('All Passed!')