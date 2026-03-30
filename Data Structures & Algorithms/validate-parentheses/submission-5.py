class Node:
    def __init__(self, num):
        self.val = num
        self.next = None

class NodeList:
    def __init__(self):
        self.left = Node(0)
    
    def add(self, num):
        newNode = Node(num)
        newNode.next = self.left.next
        self.left.next = newNode

    def isEmpty(self):
        if self.left.next == None:
            return True
        else:
            return False

    def top(self):
        return self.left.next.val
    
    def pop(self):
        self.left.next = self.left.next.next

class Solution:
    def isValid(self, s: str) -> bool:

        # solution: runtime O(n) and O(n) for space
        # store the opening brackets

        # openBrackStor = []
        stack = NodeList()

        closeBrackMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in closeBrackMap:
                # openBrackStor.append(char)
                stack.add(char)
            else:
                if (not stack.isEmpty()) and closeBrackMap[char] == stack.top():
                    # openBrackStor.pop()
                    stack.pop()
                else:
                    return False
        
        if not stack.isEmpty():
            return False

        return True

        