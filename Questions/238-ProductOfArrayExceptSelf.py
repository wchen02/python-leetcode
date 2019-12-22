# See details here https://wenshengchen.com/2019/12/10/238-product-of-array-except-self.html
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = []
        rightProduct = []

        val = 1
        for i in range(len(nums)):
            if i-1 >= 0:
                val *= nums[i-1]
            leftProduct.append(val)

        val = 1
        for i in range(len(nums)-1, -1, -1):
            if i+1 < len(nums):
                val *= nums[i+1]
            rightProduct.append(val)

        product = []
        for i in range(len(nums)):
            product.append(leftProduct[i] * rightProduct[len(nums)-1-i])

        return product

## TEST CASES
test = Solution()
answer = test.productExceptSelf([1,2,3,4])
assert answer == [24,12,8,6], answer
print('All Passed!')