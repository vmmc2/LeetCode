"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node: Optional['Node'], visited: set, nodes_map: dict) -> None:
        if node in visited:
            return
        visited.add(node)

        node_cloned = Node(node.val)
        nodes_map[node] = node_cloned

        for neighbor in node.neighbors:
            self.dfs(neighbor, visited, nodes_map)


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()
        nodes_map = {}

        self.dfs(node, visited, nodes_map)

        for og_node, clone_node in nodes_map.items():
            clone_node.neighbors = []
            for neighbor in og_node.neighbors:
                clone_node.neighbors.append(nodes_map[neighbor])

        return nodes_map[node]
        