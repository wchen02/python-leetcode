from typing import List

# See details here https://wenshengchen.com/2020/01/02/139-word-break.html
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakHelper(start: int) -> bool:
            if start == len(s):
                return True

            if canBreak[start] != None:
                return canBreak[start]

            for i in range(start, len(s)):
                if s[start:i+1] in hashmap and wordBreakHelper(i+1):
                    canBreak[start] = True
                    return True

            canBreak[start] = False
            return False

        hashmap = {}
        canBreak = [None] * len(s)

        for word in wordDict:
            hashmap[word] = True
        
        return wordBreakHelper(0)

## TEST CASES
test = Solution()
assert test.wordBreak("leetcode", ["leet", "code"]) == True
assert test.wordBreak("applepenapple", ["apple", "pen"]) == True
assert test.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
assert test.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","ba"]) == False
print('All Passed!')
