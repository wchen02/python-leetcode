from typing import List
from collections import defaultdict

# See details here https://wenshengchen.com/2020/01/09/472-concatenated-words.html
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def addWordToTrie(word: str) -> None:
            walker = head
            
            for ch in word:
                if ch not in walker.children:
                    walker.children[ch] = TrieNode()
                walker = walker.children[ch]
            walker.isWord = True

        def isConcatenatedWord(word: str, i: int) -> bool:
            nonlocal wordCount

            if i == len(word):
                return wordCount > 1

            walker = head
            
            for j in range(i, len(word)):
                ch = word[j]
                if ch not in walker.children: break
                
                walker = walker.children[ch]
                if walker.isWord:
                    wordCount += 1
                    if isConcatenatedWord(word, j+1):
                        return wordCount > 1
                    wordCount -= 1
            
            return False

        wordCount = 0
        result = []
        head = TrieNode()

        for word in words:
            addWordToTrie(word)
        
        for word in words:
            if isConcatenatedWord(word, 0):
                result.append(word)
            wordCount = 0

        return result

## TEST CASES
test = Solution()
answer = test.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
assert answer == ["catsdogcats","dogcatsdog","ratcatdogcat"], answer
answer = test.findAllConcatenatedWordsInADict(["a", "b", "ab", "abc"])
assert answer == ["ab"], answer
answer = test.findAllConcatenatedWordsInADict(["a", "aa", "aaa", "aaaaaaaaaaaaab"])
assert answer == ["aa", "aaa"], answer
print('All Passed!')
