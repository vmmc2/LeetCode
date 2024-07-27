# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        noMoreNodes = False
        head = None
        curr = None
        n = len(lists)

        while not noMoreNodes:
            nodeToBeAdded = None
            indexToBeUpdated = None
            for i in range(n):
                if lists[i] != None:
                    if nodeToBeAdded == None:
                        nodeToBeAdded = lists[i]
                        indexToBeUpdated = i
                    elif nodeToBeAdded.val > lists[i].val:
                        nodeToBeAdded = lists[i]
                        indexToBeUpdated = i
            if head == None:
                if nodeToBeAdded != None:
                    head = ListNode(val=nodeToBeAdded.val)
                    curr = head
            else:
                if nodeToBeAdded != None:
                    curr.next = ListNode(val=nodeToBeAdded.val)
                    curr = curr.next
            if indexToBeUpdated != None:
                lists[indexToBeUpdated] = lists[indexToBeUpdated].next
            noMoreNodes = True
            for i in range(n):
                if lists[i] != None: noMoreNodes = False

        return head