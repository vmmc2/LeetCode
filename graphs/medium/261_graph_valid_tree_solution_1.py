class Dsu:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def join(self, a: int, b: int) -> None:
        aRoot = self.getRoot(a)
        bRoot = self.getRoot(b)

        if self.size[aRoot] <= self.size[bRoot]:
            self.size[bRoot] += self.size[aRoot]
            self.root[aRoot] = self.root[bRoot]
        else:
            self.size[aRoot] += self.size[bRoot]
            self.root[bRoot] = self.root[aRoot]

    def getRoot(self, a: int) -> int:
        aCurr = a

        while aCurr != self.root[aCurr]:
            aCurr = self.root[aCurr]

        return aCurr

    def areConnected(self, a: int, b: int) -> bool:
        aRoot = self.getRoot(a)
        bRoot = self.getRoot(b)

        return aRoot == bRoot


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = Dsu(n)

        for edge in edges:
            if dsu.areConnected(edge[0], edge[1]):
                return False # Introducing a cycle
            else:
                dsu.join(edge[0], edge[1])

        for i in range(n):
            if dsu.size[i] == n:
                return True # There is only one component without cycles

        return False
        