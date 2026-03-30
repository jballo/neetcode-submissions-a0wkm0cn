# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists
        elif len(lists) == 0:
            return None

        return self.mergeSortHelper(lists, 0, len(lists) - 1)

    def mergeSortHelper(self, lists, left, right):
        if right <= left:
            return lists[left]

        middle = (left + right) // 2

        leftHead = self.mergeSortHelper(lists, left, middle)
        rightHead = self.mergeSortHelper(lists, middle + 1, right)

        sortedList = self.merge(leftHead, rightHead)
        return sortedList

    def merge(self, lHead, rHead):
        dummyHead = ListNode(-1)
        tail = dummyHead

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
        elif rHead:
            tail.next = rHead
        
        return dummyHead.next
            
