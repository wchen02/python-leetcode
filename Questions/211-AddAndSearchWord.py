from typing import List

# See details here https://wenshengchen.com/2020/02/16/211-add-and-search-word-data-structure-design.html
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        walker = self.root
        for ch in word:
            if ch not in walker.children:
                walker.children[ch] = TrieNode()
            walker = walker.children[ch]
        walker.isWord = True

    def searchNode(self, walker, word):
        if word == "":
            return walker.isWord

        for i in range(len(word)):
            ch = word[i]
            if ch == ".":
                for child in walker.children.values():
                    if self.searchNode(child, word[i+1:]):
                        return True
                return False
            else:
                if ch in walker.children:
                    walker = walker.children[ch]
                else:
                    return False

        return walker.isWord

    def search(self, word: str) -> bool:
        return self.searchNode(self.root, word)

## TEST CASES
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.addWord("a")
assert obj.search("pad") == False
assert obj.search("bad") == True
assert obj.search(".ad") == True
assert obj.search("..a") == False
assert obj.search("..d") == True
assert obj.search("b..") == True
assert obj.search("...") == True
assert obj.search(".a") == False
assert obj.search("a.") == False
assert obj.search("a") == True
assert obj.search(".") == True
assert obj.search("aa") == False
print('All Passed!')
