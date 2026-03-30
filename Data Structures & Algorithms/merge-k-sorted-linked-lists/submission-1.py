# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        return self.mergeSortHelper(lists, 0, len(lists) - 1)

    def mergeSortHelper(self, lists,  left, right):
        if left >= right:
            return lists[right]
        
        middle = (left + right) // 2

        lHead = self.mergeSortHelper(lists, left, middle)
        rHead = self.mergeSortHelper(lists, middle + 1, right)

        return self.merge(lHead, rHead)

    def merge(self, lHead, rHead):
        dummy = ListNode()
        tail = dummy

        while lHead and rHead:
            if lHead.val <= rHead.val:
                tail.next = lHead
                lHead = lHead.next
            else:
                tail.next = rHead
                rHead = rHead.next
            tail = tail.next
        
        if lHead:
            tail.next = lHead
        
        if rHead:
            tail.next = rHead
        
        return dummy.next
        
