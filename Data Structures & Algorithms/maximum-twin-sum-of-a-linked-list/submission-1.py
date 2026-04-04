# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        # [1, 3, 4, 9, 8, 2]

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        newHead = None

        while slow:
            temp = slow
            slow = slow.next
            temp.next = newHead
            newHead = temp
        
        maxSum = -1
        cur = head
        while newHead:
            maxSum = max(newHead.val + cur.val, maxSum)
            newHead = newHead.next
            cur = cur.next

        return maxSum


