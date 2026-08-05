from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = [[] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        order = []

        for prerequisite in prerequisites:
            adjacencyList[prerequisite[1]].append(prerequisite[0])
            inDegree[prerequisite[0]] += 1

        queue = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            currNode = queue.popleft()
            order.append(currNode)

            for neighbor in adjacencyList[currNode]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        for i in range(numCourses):
            if inDegree[i] != 0:
                return []

        return order