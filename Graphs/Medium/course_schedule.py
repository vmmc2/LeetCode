from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        answer = True
        inDegree = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            inDegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            currentNode = queue.popleft()
            for neighbors in graph[currentNode]:
                inDegree[neighbors] -= 1
                if inDegree[neighbors] == 0:
                    queue.append(neighbors)
        
        for i in range(len(inDegree)):
            if inDegree[i] != 0:
                answer = False
                break

        return answer
