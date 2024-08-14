class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Solving this problem with Bellman-Ford Algorithm.

        dist = [float("inf") for _ in range(0, n + 1)] # Node "n" must be included.
        dist[k] = 0

        for i in range(0, n - 1):
            for edge in times:
                u = edge[0]
                v = edge[1]
                w = edge[2]
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Visited every node?
        for i in range(1, n + 1):
            if dist[i] == float("inf"): return -1

        return max(dist[1:])
