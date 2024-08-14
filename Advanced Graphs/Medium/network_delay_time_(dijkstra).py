import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Solving this problem with Dijkstra's Algorithm.
        graph = [[] for _ in range(0, n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        visited = [False for _ in range(0, n + 1)]
        dist = [float("inf") for _ in range(0, n + 1)]
        dist[k] = 0

        minHeap = [(0, k)] # The initial distance to get to the source node is 0

        while len(minHeap) != 0:
            minPath, currNode = heapq.heappop(minHeap)
            if minPath == dist[currNode]:
                for neighbor, edge in graph[currNode]:
                    if minPath + edge < dist[neighbor]:
                        dist[neighbor] = minPath + edge
                        heapq.heappush(minHeap, (minPath + edge, neighbor))

        return -1 if float("inf") in dist[1:] else max(dist[1:])
