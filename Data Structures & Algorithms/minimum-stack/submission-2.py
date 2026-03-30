class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None

class MinStack:

    def __init__(self):
        self.main = Node()
        self.minStack = Node()

    def push(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.main.next
        self.main.next = newNode

        if self.minStack.next == None:
            self.minStack.next = Node(val)
        elif self.minStack.next.val < val:
            tempNode = Node(self.minStack.next.val)
            tempNode.next = self.minStack.next
            self.minStack.next = tempNode
        else:
            tempNode = Node(val)
            tempNode.next = self.minStack.next
            self.minStack.next = tempNode

    def pop(self) -> None:
        self.main.next = self.main.next.next
        self.minStack.next = self.minStack.next.next

    def top(self) -> int:
        return self.main.next.val

    def getMin(self) -> int:
        return self.minStack.next.val
