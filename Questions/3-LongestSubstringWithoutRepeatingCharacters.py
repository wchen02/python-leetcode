from typing import List

# See details here https://wenshengchen.com/2020/01/11/3-longest-substring-without-repeating-characters.html
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin, end = 0, len(s)
        startPos, longest = 0, 0
        chars = [False] * 128

        while begin < end:
            ch = ord(s[begin])
            if not chars[ch]:
                chars[ch] = True
                begin += 1
            else:
                longest = max(longest, begin - startPos)
                while chars[ch]:
                    startPosCh = ord(s[startPos])
                    chars[startPosCh] = False
                    startPos += 1
        return max(longest, begin - startPos)

## TEST CASES
test = Solution()
assert test.lengthOfLongestSubstring("abcabcbb") == 3
assert test.lengthOfLongestSubstring("bbbbb") == 1
assert test.lengthOfLongestSubstring("pwwkew") == 3
assert test.lengthOfLongestSubstring("") == 0
assert test.lengthOfLongestSubstring("a") == 1
assert test.lengthOfLongestSubstring(" ") == 1
print('All Passed!')
