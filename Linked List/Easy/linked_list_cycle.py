# Floyd's Tortoise and Hare Algorithm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head
        if fastPointer != None:
            fastPointer = head.next

        while slowPointer != None and fastPointer != None:
            if slowPointer == fastPointer:
                return True
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
            if fastPointer != None:
                fastPointer = fastPointer.next


        return False
