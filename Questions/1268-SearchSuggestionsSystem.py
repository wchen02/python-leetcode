import bisect
from typing import List

# See details here https://wenshengchen.com/2020/02/12/1268-search-suggestions-system.html
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggestions = []
        for j in range(1, len(searchWord)+1):
            wordSuggestions = []
            index = bisect.bisect_left(products, searchWord[:j])
            for i in range(3):
                if index+i < len(products) and products[index+i].startswith(searchWord[:j]):
                    wordSuggestions.append(products[index+i])
            suggestions.append(wordSuggestions)
        return suggestions

## TEST CASES
test = Solution()
assert test.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse") == [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
]
assert test.suggestedProducts(["havana"], "havana") == [
    ["havana"],
    ["havana"],
    ["havana"],
    ["havana"],
    ["havana"],
    ["havana"]
]
assert test.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags") == [
    ["baggage","bags","banner"],
    ["baggage","bags","banner"],
    ["baggage","bags"],
    ["bags"]
]
assert test.suggestedProducts(["havana"], "tatiana") == [[],[],[],[],[],[],[]]
print('All Passed!')
