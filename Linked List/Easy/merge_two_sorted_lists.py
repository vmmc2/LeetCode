# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head3 = None
        current = head3
        
        while head1 != None and head2 != None:
            val1 = head1.val
            val2 = head2.val
            if val1 <= val2:
                if head3 == None:
                    head3 = ListNode(val=val1)
                    current = head3
                else:
                    current.next = ListNode(val=val1)
                    current = current.next
                head1 = head1.next
            else:
                if head3 == None:
                    head3 = ListNode(val=val2)
                    current = head3
                else:
                    current.next = ListNode(val=val2)
                    current = current.next
                head2 = head2.next

        while head1 != None:
            if head3 == None:
                head3 = ListNode(val=head1.val)
                current = head3
            else:
                current.next = ListNode(val=head1.val)
                current = current.next
            head1 = head1.next


        while head2 != None:
            if head3 == None:
                head3 = ListNode(val=head2.val)
                current = head3
            else:
                current.next = ListNode(val=head2.val)
                current = current.next
            head2 = head2.next

        return head3
