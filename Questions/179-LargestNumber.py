from typing import List

# See details here https://wenshengchen.com/2020/01/20/179-largest-number.html
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y < y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey, reverse=True))
        return '0' if largest_num[0] == '0' else largest_num

## TEST CASES
test = Solution()
answer = test.largestNumber([10,2])
assert answer == "210", answer
answer = test.largestNumber([3,30,34,5,9])
assert answer == "9534330", answer
answer = test.largestNumber([1,10,100])
assert answer == "110100", answer
answer = test.largestNumber([1,10,100,1000])
assert answer == "1101001000", answer
answer = test.largestNumber([1,10,11])
assert answer == "11110", answer
answer = test.largestNumber([1,10,11,100,101,110,111])
assert answer == "11111111010110100", answer
answer = test.largestNumber([1,10,11,100,101,110,111,2,20,200])
assert answer == "22020011111111010110100", answer
answer = test.largestNumber([1,10,100,1020])
assert answer == "1102010100", answer
answer = test.largestNumber([1,19,119,191])
assert answer == "191911191", answer
print('All Passed!')
