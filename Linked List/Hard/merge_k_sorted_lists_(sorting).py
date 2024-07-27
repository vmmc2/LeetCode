# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        nodes = []
        head = None
        curr = None

        for i in range(0, n):
            curr = lists[i]
            while curr != None:
                nodes.append(curr.val)
                curr = curr.next
        nodes.sort()

        for i in range(0, len(nodes)):
            if head == None:
                head = ListNode(val=nodes[i])
                curr = head
            else:
                curr.next = ListNode(val=nodes[i])
                curr = curr.next

        return head