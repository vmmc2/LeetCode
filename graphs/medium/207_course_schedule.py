from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = [[] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adjacencyList[prerequisite[1]].append(prerequisite[0])
            inDegree[prerequisite[0]] += 1

        queue = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            currNode = queue.popleft()

            for neighbor in adjacencyList[currNode]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        for i in range(numCourses):
            if inDegree[i] != 0:
                return False

        return True
        