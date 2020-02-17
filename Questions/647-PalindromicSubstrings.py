from typing import List

# See details here https://wenshengchen.com/2020/02/14/647-palindromic-substrings.html
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])

                if dp[i][j]:
                    count += 1

        return count
                                
## TEST CASES
test = Solution()
assert test.countSubstrings("abc") == 3
assert test.countSubstrings("aaa") == 6
assert test.countSubstrings("beb") == 4
assert test.countSubstrings("bebe") == 6
assert test.countSubstrings("aaaaaaa") == 28
assert test.countSubstrings("aacaaeadaa") == 17
print('All Passed!')
