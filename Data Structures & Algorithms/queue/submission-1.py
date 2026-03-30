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
        if self.left.next == self.right:
            return True
        return False

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
        if self.right.prev == self.left:
            return -1
        
        node = self.right.prev
        self.right.prev = node.prev
        node.prev.next = self.right
        return node.val

    def popleft(self) -> int:
        if self.left.next == self.right:
            return -1
        
        node = self.left.next
        self.left.next = node.next
        node.next.prev = self.left
        return node.val
