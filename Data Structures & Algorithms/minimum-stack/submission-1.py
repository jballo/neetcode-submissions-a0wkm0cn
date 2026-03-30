class Node:
    def __init__(self, num=0):
        self.val = num
        self.next = None

class NodeList:
    def __init__(self):
        self.left = Node()
    
    def prepend(self, num):
        newNode = Node(num)
        newNode.next = self.left.next
        self.left.next = newNode

    def pop(self):
        self.left.next = self.left.next.next

    def top(self):
        return self.left.next.val
    

class MinStack:

    def __init__(self):
        self.main = NodeList()
        self.minList = NodeList()
        

    def push(self, val: int) -> None:
        if self.minList.left.next and self.minList.top() < val:
            self.minList.prepend(self.minList.top())
        else:
            self.minList.prepend(val)
        self.main.prepend(val)

    def pop(self) -> None:
        self.main.pop()
        self.minList.pop()

    def top(self) -> int:
        return self.main.top()

    def getMin(self) -> int:
        return self.minList.top()        
