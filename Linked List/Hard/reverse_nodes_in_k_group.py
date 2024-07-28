# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, beginNode: Optional[ListNode], endNode: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = beginNode
        next = curr.next

        while curr != endNode:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
            curr.next = prev

        newHead = endNode
        newTail = beginNode

        return (newHead, newTail)

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
                curr = curr.next
            elif currK == k:
                endNode = curr
                curr = curr.next
                newHead, newTail = self.reverseGroup(beginNode, endNode)
                beginNode = None
                endNode = None
                kGroups.append((newHead, newTail))
                currK = 0
            else:
                curr = curr.next
            currK += 1
        if beginNode != None and endNode == None:
            kGroups.append((beginNode, endNode))

        if len(kGroups) == 1:
            return kGroups[0][0]
        else:
            newHead = kGroups[0][0]
            for i in range(0, len(kGroups) - 1):
                kGroups[i][1].next = kGroups[i + 1][0]

            return newHead

