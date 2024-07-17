import heapq

class Stone:
    def __init__(self, weight):
        self.weight = weight
    
    def __lt__(self, other):
        return self.weight >= other.weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [Stone(weight) for weight in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heavy1 = heapq.heappop(heap)
            heavy2 = heapq.heappop(heap)
            if heavy1.weight != heavy2.weight:
                newStone = Stone(max(heavy1.weight, heavy2.weight) - min(heavy1.weight, heavy2.weight))
                heapq.heappush(heap, newStone)

        if len(heap) == 0:
            return 0
        return heap[0].weight
