from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        graph = defaultdict(list) # Adjacency List: Possible patterns -> [words that fall into that pattern]

        wordList.append(beginWord)

        for word in wordList:
            for j in range(0, len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        distance = {beginWord: 1}

        while len(queue) != 0:
            currWord = queue.popleft()
            for i in range(0, len(currWord)): # Finding the neighbours of the current word
                pattern = currWord[:i] + "*" + currWord[i + 1:]
                for neighbour in graph[pattern]:
                    if not neighbour in visited:
                        visited.add(neighbour)
                        distance[neighbour] = distance[currWord] + 1
                        queue.append(neighbour)

        return distance[endWord] if endWord in distance else 0
