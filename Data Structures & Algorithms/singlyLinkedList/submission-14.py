class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.left = self.tail = Node()
    
    def get(self, index: int) -> int:
        i = 0
        temp = self.left.next
        while temp and i < index:
            temp = temp.next
            i += 1

        if temp and i == index:
            return temp.val
        
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.left.next
        self.left.next = newNode

        if self.left == self.tail:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        temp = self.left
        while temp and i < index:
            temp = temp.next
            i += 1

        if temp and temp.next and i == index:
            target = temp.next
            temp.next = temp.next.next
            if target == self.tail:
                self.tail = temp
            return True

        return False

    def getValues(self) -> List[int]:
        vals = []
        temp = self.left.next
        while temp:
            vals.append(temp.val)
            temp = temp.next

        return vals
