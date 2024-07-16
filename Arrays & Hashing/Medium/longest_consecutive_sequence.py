from collections import defaultdict

class Solution:
    def dfs(self, vertex: int, graph: defaultdict, visited: defaultdict, componentSize: int) -> None:
        visited[vertex] = True
        componentSize[0] += 1
        
        for neighbor in graph[vertex]:
            if(neighbor not in visited):
                self.dfs(neighbor, graph, visited, componentSize)

        return

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        graph = { }
        visited = { }
    
        for i in range(0, n):
            vertex = nums[i]
            if vertex in graph:
                continue
            graph[vertex] = []
            if(vertex - 1 in graph):
                graph[vertex].append(vertex - 1)
                graph[vertex - 1].append(vertex)
            if(vertex + 1 in graph):
                graph[vertex].append(vertex + 1)
                graph[vertex + 1].append(vertex)

        answer = 0
        for i in range(0, n):
            vertex = nums[i]
            if(vertex in visited):
                continue
            current = [0]
            self.dfs(vertex, graph, visited, current)
            answer = max(answer, current[0])

        return answer
