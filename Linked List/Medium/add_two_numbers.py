# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        l3 = None
        curr3 = l3
        carry = 0

        while curr1 and curr2:
            sum = curr1.val + curr2.val + carry
            digit = sum % 10
            carry = sum // 10
            if l3 == None:
                l3 = ListNode(digit)
                curr3 = l3
            else:
                curr3.next = ListNode(digit)
                curr3 = curr3.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1 != None:
            sum = curr1.val + carry
            digit = sum % 10
            carry = sum // 10
            curr3.next = ListNode(digit)
            curr3 = curr3.next
            curr1 = curr1.next
        while curr2 != None:
            sum = curr2.val + carry
            digit = sum % 10
            carry = sum // 10
            curr3.next = ListNode(digit)
            curr3 = curr3.next
            curr2 = curr2.next

        if carry == 1:
            curr3.next = ListNode(carry)

        return l3
