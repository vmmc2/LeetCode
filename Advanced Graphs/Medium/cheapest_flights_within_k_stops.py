class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Solving with a variation of Bellman-Ford algorithm
        distance = [float("inf") for _ in range(0, n)]
        distance[src] = 0

        for i in range(0, k + 1):
            layerDistance = distance[:] # If you need a copy of a list use this notation. Remember: Python uses references for list, dicts, sets.
            for u, v, price in flights:
                if distance[u] + price < layerDistance[v]:
                    layerDistance[v] = distance[u] + price

            distance = layerDistance


        return -1 if distance[dst] == float("inf") else distance[dst]
