from typing import List

# See details here https://wenshengchen.com/2020/01/06/227-basic-calculator-ii.html
class Solution:
    def calculate(self, s: str) -> int:
        result, num = 0, 0
        stk = []
        operation = "+"

        for i in range(len(s)):
            if s[i] >= "0" and s[i] <= "9":
                num = num * 10 + int(s[i])
            if s[i] in ["+", "-", "*", "/"] or i == len(s) - 1:
                if operation == "+":
                    stk.append(num)
                elif operation == "-":
                    stk.append(-num)
                elif operation == "*":
                    stk.append(stk.pop()*num)
                elif operation == "/":
                    left = stk.pop()
                    right = num
                    sign = 1 if left > 0 else -1
                    sign = sign * (1 if right > 0 else -1)
                    stk.append((abs(left)//abs(right)) * sign)
                operation = s[i]
                num = 0

        while stk:
            result += stk.pop()

        return result

## TEST CASES
test = Solution()
# assert test.calculate("3+2*2") == 7
# assert test.calculate(" 3/2 ") == 1
# assert test.calculate(" 3+5 / 2 ") == 5
# assert test.calculate("1+2* 3 /4 - 5 +6*7/8 -   9") == -7
assert test.calculate("14-3/2") == 13
print('All Passed!')
