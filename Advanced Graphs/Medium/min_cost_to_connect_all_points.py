class Dsu:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

    def find(self, node: int) -> int:
        curr = node
        while curr != self.parent[curr]:
            curr = self.parent[curr]

        return curr

    def connect(self, a: int, b: int) -> None:
        aParent = self.find(a)
        bParent = self.find(b)

        self.parent[bParent] = aParent

    def areConnected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

class Solution:
    def createEdge(self, a: List[int], b: List[int]) -> tuple:
        edgeCost = abs(a[0] - b[0]) + abs(a[1] - b[1])

        return (edgeCost, a, b)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = Dsu(n)
        labelPointNode = {}

        for i in range(n):
            labelPointNode[(points[i][0], points[i][1])] = i

        edges = [ ]

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                currEdge = self.createEdge(points[i], points[j])
                edges.append(currEdge)

        edges.sort()

        takenEdges = 0
        minCost = 0
        edgeIdx = 0
        while takenEdges < n - 1:
            currentEdge = edges[edgeIdx]
            nodeA = labelPointNode[tuple(edges[edgeIdx][1])]
            nodeB = labelPointNode[tuple(edges[edgeIdx][2])]
            if not dsu.areConnected(nodeA, nodeB):
                dsu.connect(nodeA, nodeB)
                takenEdges += 1
                minCost += currentEdge[0]
            edgeIdx += 1

        return minCost
