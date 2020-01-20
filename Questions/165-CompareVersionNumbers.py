from typing import List

# See details here https://wenshengchen.com/2020/01/18/165-compare-version-numbers.html
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        i, j = 0, 0

        while i < len(v1) or j < len(v2):
            subVersion1 = int(v1[i]) if i < len(v1) else 0
            subVersion2 = int(v2[j]) if j < len(v2) else 0

            if subVersion1 > subVersion2:
                return 1
            elif subVersion1 < subVersion2:
                return -1
            else:
                i += 1
                j += 1

        return 0

## TEST CASES
test = Solution()
assert test.compareVersion("0.1", "1.1") == -1
assert test.compareVersion("1.0.1", "1") == 1
assert test.compareVersion("7.5.2.4", "7.5.3") == -1
assert test.compareVersion("1.01", "1.001") == 0
assert test.compareVersion("1.0", "1.0.0") == 0
print('All Passed!')
