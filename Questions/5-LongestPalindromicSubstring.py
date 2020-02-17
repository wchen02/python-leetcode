from typing import List

# See details here https://wenshengchen.com/2020/02/17/5-longest-palindromic-substring.html
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        longest = -1
        longestPalindrome = ""

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                print(i, j)
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
                if dp[i][j] and j-i > longest:
                    longest = j-i
                    longestPalindrome = s[i:j+1]
                    print(i, j, dp[i][j], longest, longestPalindrome)

        return longestPalindrome

## TEST CASES
test = Solution()
assert ["bab", "aba"].index(test.longestPalindrome("babad")) >= 0
# assert test.longestPalindrome("cbbd") == "bb"
# assert test.longestPalindrome("abcda") == "a"
print('All Passed!')
