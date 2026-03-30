# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = dummyTail = ListNode()


        while list1 and list2:
            if list1.val < list2.val:
                tempNext = list1.next
                list1.next = dummyTail.next
                dummyTail.next = list1
                list1 = tempNext
            else:
                tempNext = list2.next
                list2.next = dummyTail.next
                dummyTail.next = list2
                list2 = tempNext
            dummyTail = dummyTail.next
        
        if list1:
            dummyTail.next = list1
        elif list2:
            dummyTail.next = list2

        return dummyHead.next

