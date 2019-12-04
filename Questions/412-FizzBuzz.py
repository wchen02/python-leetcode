from typing import List

# See details here https://wenshengchen.com/2019/12/04/412-fizz-buzz.html
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n + 1):
            newStr = str(i)
            
            if i % 15 == 0:
                newStr = 'FizzBuzz'
            elif i % 3 == 0:
                newStr = 'Fizz'
            elif i % 5 == 0:
                newStr = 'Buzz'
            
            res.append(newStr)

        return res

## TEST CASES
test = Solution()
answer = test.fizzBuzz(3)
assert answer == [
    '1',
    '2',
    'Fizz'
], answer

answer = test.fizzBuzz(5)
assert answer == [
    '1',
    '2',
    'Fizz',
    '4',
    'Buzz'
], answer

answer = test.fizzBuzz(15)
assert answer == [
    '1',
    '2',
    'Fizz',
    '4',
    'Buzz',
    'Fizz',
    '7',
    '8',
    'Fizz',
    'Buzz',
    '11',
    'Fizz',
    '13',
    '14',
    'FizzBuzz'
], answer

print('All Passed!')
