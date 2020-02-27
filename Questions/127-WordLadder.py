from typing import Dict, List
from collections import defaultdict, deque

# See details here https://wenshengchen.com/2020/02/26/127-word-ladder.html
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbors = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                neighbors[word[:i] + '-' + word[i+1:]].append(word)
        
        hops = 0
        q = deque([beginWord])
        visited = set([])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == endWord:
                    return hops + 1
                for i in range(len(node)):
                    key = node[:i] + '-' + node[i+1:]

                    for neighbor in neighbors[key]:
                        if neighbor not in visited:
                            q.append(neighbor)
            hops += 1
        return 0

## TEST CASES
test = Solution()
assert test.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert test.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
print('All Passed!')
