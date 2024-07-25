# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        numElements = 0
        curr = head
        
        while curr != None:
            numElements += 1
            curr = curr.next

        if numElements == n:
            head = head.next
            return head
        else:
            curr = head
            while numElements != n + 1:
                numElements -= 1
                curr = curr.next

            curr.next = curr.next.next
            return head
