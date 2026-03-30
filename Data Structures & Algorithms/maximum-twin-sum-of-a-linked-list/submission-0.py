# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 2
        # 4
        # 6
        # [0, 1, 2, 3, 4, 5]
        # 5 -> 0
        # 4 -> 1
        # 3 -> 2

        nodeArr = []

        temp = head
        while temp:
            nodeArr.append(temp)
            temp = temp.next

        
        L = 0
        R = len(nodeArr)-1
        maxTwin = 0

        while L < R and L <= (len(nodeArr) / 2 - 1):
          maxTwin = max(maxTwin, (nodeArr[L].val + nodeArr[R].val))  
          L += 1
          R -= 1
        
        return maxTwin

