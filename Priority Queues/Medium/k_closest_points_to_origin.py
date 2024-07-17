import heapq

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return ((self.x)**2 + (self.y)**2) < ((other.x)**2 + (other.y)**2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer = []
        heap = [Point(point[0], point[1]) for point in points]

        heapq.heapify(heap)

        while len(answer) != k:
            answer.append(heapq.heappop(heap))

        answer = [[point.x, point.y] for point in answer]

        return answer
