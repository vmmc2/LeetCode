from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canCreateEdge(word1: str, word2: str) -> bool:
            if len(word1) != len(word2):
                return False
            else:
                n = len(word1)
                diff = 0
                for i in range(0, n):
                    if word1[i] != word2[i]:
                        diff += 1
                        if diff > 1: return False
                return True if diff == 1 else False


        if not endWord in wordList:
            return 0

        wordToNode = {}
        wordList.insert(0, beginWord)
        n = len(wordList)

        for i in range(0, n):
            wordToNode[wordList[i]] = i

        graph = [[] for _ in range(0, n)]

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if canCreateEdge(wordList[i], wordList[j]):
                    graph[wordToNode[wordList[i]]].append(wordToNode[wordList[j]])
                    graph[wordToNode[wordList[j]]].append(wordToNode[wordList[i]])

        visited = [False for _ in range(0, n)]
        distance = [float("inf") for _ in range(0, n)]
        
        # Running bfs
        distance[wordToNode[beginWord]] = 0
        queue = deque()

        queue.append(wordToNode[beginWord])

        while len(queue) != 0:
            currNode = queue.popleft()
            visited[currNode] = True
            for neighbour in graph[currNode]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    distance[neighbour] = 1 + distance[currNode]
                    queue.append(neighbour)

        return 0 if distance[wordToNode[endWord]] == float("inf") else distance[wordToNode[endWord]] + 1
