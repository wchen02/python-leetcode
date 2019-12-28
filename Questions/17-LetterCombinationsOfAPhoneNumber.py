from typing import List

# See details here https://wenshengchen.com/2019/12/26/17-letter-combinations-of-a-phone-number.html
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(curString: List[str], i: int) -> None:
            nonlocal digitLetterMap, combos

            if i == len(digits):
                combos.append("".join(curString))
                return

            for letter in digitLetterMap[int(digits[i])]:
                curString[i] = letter
                helper(curString, i+1)

        if not digits: return []
        digitLetterMap = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        combos = []
        helper([None]*len(digits), 0)
        return combos

## TEST CASES
test = Solution()
assert test.letterCombinations('23') == [
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf"
]
assert test.letterCombinations('') == []
print('All Passed!')
