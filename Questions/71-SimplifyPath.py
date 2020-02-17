from typing import List

# See details here https://wenshengchen.com/2020/02/15/71-simplify-path.html
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        absPath = []
        
        for part in parts:
            if part == '..':
                if absPath:
                    absPath.pop()
            elif part == '' or part == '.':
                continue
            else:
                absPath.append(part)

        return "/" + "/".join(absPath)

## TEST CASES
test = Solution()
assert test.simplifyPath("/home/") == "/home"
assert test.simplifyPath("/../") == "/"
assert test.simplifyPath("/home//foo/") == "/home/foo"
assert test.simplifyPath("/a/./b/../../c/") == "/c"
assert test.simplifyPath("/a/../../b/../c//.//") == "/c"
assert test.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
print('All Passed!')
