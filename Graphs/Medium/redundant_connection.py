class Dsu:
    def __init__(self, n: int):
        self.dsu = [i for i in range(0, n + 1)]

    def find(self, a: int) -> int:
        curr = a
        while curr != self.dsu[curr]:
            curr = self.dsu[curr]
        return curr

    def areConnected(self, a: int, b: int) -> bool:
        aParent = self.find(a)
        bParent = self.find(b)
        return aParent == bParent

    def connect(self, a: int, b: int) -> None:
        aParent = self.find(a)
        bParent = self.find(b)
        self.dsu[bParent] = self.dsu[aParent]
        return None  


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = Dsu(len(edges))
        answer = [ ]

        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]

            if dsu.areConnected(a, b):
                answer = edges[i]
            else:
                dsu.connect(a, b)

        return answer
