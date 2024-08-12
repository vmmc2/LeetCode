"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            if node in oldToNew: # A clone already exists. Return the clone
                return oldToNew[node]

            copy = Node(val=node.val, neighbors=[]) # Create the clone and register it.
            oldToNew[node] = copy

            for neigh in node.neighbors:
                copy.neighbors.append(clone(neigh)) # The trick lies here.

            return copy

        return clone(node) if node else None
