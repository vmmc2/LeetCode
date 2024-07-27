# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, beginNode: Optional[ListNode], endNode: Optional[ListNode]) -> Optional[ListNode]:

        return newHead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        kGroups = []
        curr = head
        currK = 1

        beginNode = None
        endNode = None

        while curr != None:
            if currK == 1:
                beginNode = curr
            elif currK == k:
                endNode = curr
                newHead = self.reverseGroup(beginNode, endNode)
                kGroups.append(newHead)
                currK = 0
            currK += 1
            curr = curr.next
