from typing import List

# See details here https://wenshengchen.com/2020/01/06/34-find-first-and-last-position-of-element-in-sorted-array.html
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        ret = [-1, -1]

        if not nums: return ret
        
        while lo < hi:
            mid = lo + (hi-lo) // 2

            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        if nums[lo] == target:
            ret[0] = lo
        else:
            return ret
        
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi-lo) // 2 + 1

            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid

        ret[1] = hi
        return ret

## TEST CASES
test = Solution()
assert test.searchRange([5,7,7,8,8,10], 8) == [3,4]
assert test.searchRange([5,7,7,8,8,10], 6) == [-1,-1]
assert test.searchRange([5,7,7,8,8,10], 5) == [0,0]
assert test.searchRange([5,7,7,8,8,10], 10) == [5,5]
assert test.searchRange([5,5,5,5,5,7,7,8,8,10], 5) == [0,4]
assert test.searchRange([5,5,5,5,5,7,7,8,8,10],7) == [5,6]
assert test.searchRange([],0) == [-1,-1]
assert test.searchRange([1],0) == [-1,-1]
assert test.searchRange([1],1) == [0,0]
assert test.searchRange([1,1],1) == [0,1]
print('All Passed!')
