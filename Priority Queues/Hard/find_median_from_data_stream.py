import heapq

class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            valueFromMaxHeap = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -valueFromMaxHeap)

        if len(self.maxHeap) != 0 and len(self.minHeap) != 0 and -self.maxHeap[0] > self.minHeap[0]:
            valueFromMaxHeap = heapq.heappop(self.maxHeap)
            valueFromMinHeap = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, -valueFromMaxHeap)
            heapq.heappush(self.maxHeap, -valueFromMinHeap)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            valueMinHeap = self.minHeap[0]
            valueMaxHeap = -self.maxHeap[0]
            return (valueMinHeap + valueMaxHeap) / 2
        else:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()