class Solution:
    def dfs(self, adjacencyList: List[List[int]], visited: List[bool], node: int) -> None:
        visited[node] = True

        for neighbor in adjacencyList[node]:
            if not visited[neighbor]:
                self.dfs(adjacencyList, visited, neighbor)

        return


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        answer = 0

        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])

        for i in range(n):
            if not visited[i]:
                answer += 1
                self.dfs(adjacencyList, visited, i)

        return answer

