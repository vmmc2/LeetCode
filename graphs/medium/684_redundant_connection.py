class Dsu:
    def __init__(self, nodes: int):
        self.root = [i for i in range(nodes + 1)] # In the beginning, each node is root of itself.

    def find(self, a: int) -> int:
        curr = a
        while curr != self.root[curr]: # Navigating up the chain...
            curr = self.root[curr]

        return curr

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)

        self.root[root_b] = self.root[root_a]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = Dsu(len(edges))
        answer = None

        for edge in edges:
            if dsu.find(edge[0]) == dsu.find(edge[1]): # Already connected
                answer = edge
            else: # Not connected. Must perform union.
                dsu.union(edge[0], edge[1])

        return answer
        