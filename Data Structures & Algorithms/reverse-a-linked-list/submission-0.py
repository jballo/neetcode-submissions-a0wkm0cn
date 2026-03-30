# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #understand
        # can we assume we will have an empty list
        # can we take an iterative approach?
        # do we have any space or time constraints?
        #match: using a two pointer technique seems appropriate
        #plan
        # create a pointer called newHead that is set None
        newHead = None
        # while head is valid
        while head:
            # store tempNext to head's next
            headNext = head.next
            # create a pointer called newTempHead to head
            newTempHead = head
            # have newTempHead's next point to newHead
            newTempHead.next = newHead
            # set newTempHead as newHead
            newHead = newTempHead
            # set head as tempNext
            head = headNext
        # return newHead
        return newHead
        #implement
        #review: solution for time is O(N) and space O(1)
        #evaluate: current implementation for iterative is as fast as can be
        # another approach could be recursive approach instead