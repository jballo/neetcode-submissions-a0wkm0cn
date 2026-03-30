# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newDummy = ListNode()

        while head:
            tempNext = head.next
            head.next = newDummy.next
            newDummy.next = head
            head = tempNext
        
        return newDummy.next
