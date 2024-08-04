from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = defaultdict(int)
        queue = deque()

        for task in tasks:
            taskFreq[task] += 1

        maxHeap = []
        
        for task, freq in taskFreq.items():
            maxHeap.append(-freq)
        heapq.heapify(maxHeap)

        time = 0
        while len(maxHeap) != 0 or len(queue) != 0:
            time += 1
            if len(maxHeap) != 0:
                currTaskFreq = heapq.heappop(maxHeap)
                if currTaskFreq + 1 != 0:
                    queue.append((currTaskFreq + 1, time + n))
            
            if len(queue) != 0 and queue[0][1] == time:
                (taskFreq, nextPossibleTime) = queue.popleft()
                heapq.heappush(maxHeap, taskFreq)

        return time
