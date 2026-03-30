class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right
        
    def append(self, value: int) -> None:
        newNode = Node(value)
        newNode.next = self.right
        newNode.prev = self.right.prev
        self.right.prev.next = newNode
        self.right.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        newNode.next = self.left.next
        newNode.prev = self.left
        self.left.next.prev = newNode
        self.left.next = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        lastNode = self.right.prev
        lastNode.prev.next = self.right
        self.right.prev = lastNode.prev
        return lastNode.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        firstNode = self.left.next
        self.left.next = firstNode.next
        firstNode.next.prev = self.left
        return firstNode.val
        
