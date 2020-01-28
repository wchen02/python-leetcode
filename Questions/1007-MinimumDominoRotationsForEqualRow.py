from typing import List

# See details here https://wenshengchen.com/2020/01/23/1007-minimum-domino-rotations-for-equal-row.html
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def solutionExists(digit: int) -> int:
            countA, countB = 0, 0

            for i in range(len(A)):
                if A[i] == B[i] == digit:
                    continue
                elif A[i] == digit:
                    countA += 1
                elif B[i] == digit:
                    countB += 1
                else:
                    return -1
            
            return min(countA, countB)
        
        solutionA = solutionExists(A[0])
        solutionB = solutionExists(B[0])
        
        if solutionA == solutionB == -1:
            return -1
        elif solutionA == -1 or solutionB == -1:
            return max(solutionA, solutionB)
        else:
            return min(solutionA, solutionB)

## TEST CASES
test = Solution()
assert test.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]) == 2
assert test.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]) == -1
print('All Passed!')
