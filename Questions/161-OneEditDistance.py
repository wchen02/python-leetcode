from typing import List

# See details here https://wenshengchen.com/2020/01/19/161-one-edit-distance.html
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        lenS, lenT = len(s), len(t)
        if abs(lenS - lenT) > 1: return False

        if lenS < lenT:
            return self.isOneEditDistance(t, s) # Insert

        for i in range(lenS):
            if i == lenT or s[i] != t[i]:
                if lenS == lenT: # Replace
                    return s[:i] + t[i] + s[i+1:] == t
                elif lenS > lenT: # Delete
                    return s[:i] + s[i+1:] == t
        return False

## TEST CASES
test = Solution()
assert test.isOneEditDistance("ab", "acb") == True
assert test.isOneEditDistance("cab", "ad") == False
assert test.isOneEditDistance("1203", "1213") == True
assert test.isOneEditDistance("teacher", "treacher") == True
assert test.isOneEditDistance("a", "") == True
assert test.isOneEditDistance("a", "ab") == True
assert test.isOneEditDistance("ac", "ab") == True
print('All Passed!')
