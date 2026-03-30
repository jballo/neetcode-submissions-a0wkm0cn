# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = ListNode()
        tail = None

        while list1 and list2:
            lowerHead = None
            if list1.val < list2.val:
                lowerHead = list1
                list1 = list1.next
            else:
                lowerHead = list2
                list2 = list2.next
            
            if left.next == None:
                left.next = lowerHead
                tail = lowerHead
            else:
                tail.next = lowerHead
                tail = tail.next
        
        if list1:
            if left.next == None:
                left.next = list1
            else:
                tail.next = list1
        elif list2:
            if left.next == None:
                left.next = list2
            else:
                tail.next = list2
        
        return left.next
            