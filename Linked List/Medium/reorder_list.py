# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, begin: ListNode) -> ListNode:
        prev = None
        curr = begin
        nxt = begin.next

        while nxt != None:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
            curr.next = prev

        return curr

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return
        else:
            slow = head
            fast = head.next

            while fast.next != None:
                slow = slow.next
                fast = fast.next
                if fast.next != None:
                    fast = fast.next

            reversedSndHalf = self.reverseList(slow.next)
            slow.next = None
            fstHalf = head

            while fstHalf != None and reversedSndHalf != None:
                nxtSndHalf = reversedSndHalf.next
                
                reversedSndHalf.next = fstHalf.next
                fstHalf.next = reversedSndHalf

                fstHalf = fstHalf.next.next
                reversedSndHalf = nxtSndHalf

        return