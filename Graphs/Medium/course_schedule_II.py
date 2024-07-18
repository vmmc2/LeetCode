from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        coursesOrder = []
        graph = [[] for i in range(numCourses)]
        inDegree = [0 for i in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            inDegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            currNode = queue.popleft()
            coursesOrder.append(currNode)

            for neighbor in graph[currNode]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        for i in range(numCourses):
            if inDegree[i] != 0:
                return [ ]

        return coursesOrder
