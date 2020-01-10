from typing import List

# See details here https://wenshengchen.com/2020/01/08/150-evaluate-reverse-polish-notation.html
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evalExpression() -> int:
            token = tokens.pop()

            if token not in ['+','-','*','/']:
                return int(token)

            num2 = evalExpression()
            num1 = evalExpression()
            
            if token == "+":
                return num1 + num2
            elif token == "-":
                return num1 - num2
            elif token == "*":
                return num1 * num2
            else:
                return int(num1 / num2)

        return evalExpression()

## TEST CASES
test = Solution()
assert test.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert test.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert test.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
print('All Passed!')
