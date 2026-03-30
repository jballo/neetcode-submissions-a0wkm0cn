# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lPtr = head # 4
        rPtr = head # None
        # [1,2,3,4,5,6]
        while lPtr != None and rPtr != None and rPtr.next != None:
            lPtr = lPtr.next
            rPtr = rPtr.next.next

        return lPtr