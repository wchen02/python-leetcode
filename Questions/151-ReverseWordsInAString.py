from typing import List, Set

# See details here https://wenshengchen.com/2020/02/24/151-reverse-words-in-a-string.html
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        res = []
        for i in range(len(words)-1, -1, -1):
            if words[i]:
                res.append(words[i])
        
        return " ".join(res)

## TEST CASES
test = Solution()
assert test.reverseWords("the sky is blue") == "blue is sky the"
assert test.reverseWords("  hello world!  ") == "world! hello"
assert test.reverseWords("a good   example") == "example good a"
print('All Passed!')
