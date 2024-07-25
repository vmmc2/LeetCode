"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        curr1 = head
        head2 = None
        curr2 = head

        while curr1 != None:
            if head2 == None:
                head2 = Node(x=curr1.val)
                curr2 = head2
            else:
                curr2.next = Node(x=curr1.val)
                curr2 = curr2.next

            nodeMap[curr1] = curr2
            curr1 = curr1.next

        curr1 = head
        curr2 = head2
        while curr1 != None:
            randomPointer = curr1.random
            if randomPointer == None:
                curr2.random = None
            else:
                newRandomPointer = nodeMap[randomPointer]
                curr2.random = newRandomPointer
            curr1 = curr1.next
            curr2 = curr2.next

        return head2
