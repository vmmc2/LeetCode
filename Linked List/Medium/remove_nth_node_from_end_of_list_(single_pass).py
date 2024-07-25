# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes = [ ]

        while curr != None:
            nodes.append(curr)
            curr = curr.next

        if n == len(nodes):
            head = head.next
        else:
            numNodes = len(nodes)
            idx = numNodes - n - 1
            nodes[idx].next = nodes[idx + 1].next

        return head
