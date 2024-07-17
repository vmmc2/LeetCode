import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minHeap = []
        heapq.heapify(minHeap)

        for i in range(0, n):
            heapq.heappush(minHeap, nums[i])
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
