# Iterative Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head != None and head.next == None):
            return head

        predecessor = None
        current = head
        successor = head.next

        while successor != None:
            current.next = predecessor
            predecessor = current
            current = successor
            successor = successor.next
            current.next = predecessor

        return current
