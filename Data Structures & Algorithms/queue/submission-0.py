# Understand
# Are we allowed to use other data structures?
# Am I limited to a certain space complexity?
# Am I able to use a doubly linked list?
# am I able to import libraries or data structures?


# Declare class for doubly node
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        # initalize the doubly linked list attributes
        # using left and right dummy pointer technique
        self.left = Node(-1)
        self.right = Node(-1)
        # set dummy nodes pointing to eachother
        self.left.next = self.right
        self.right.prev = self.left


    def isEmpty(self) -> bool:
        # check if doubly linked list is empty
        # return true if dummy nodes are pointing to eachother
        return self.left.next == self.right
        

    def append(self, value: int) -> None:
        # for our implementation, the tail will be the end
        # create new node
        newNode = Node(value)
        # declare variable to the old tail
        oldTail = self.right.prev
        # new node's prev will point to old tail
        newNode.prev = oldTail
        # new node's next will point to right
        newNode.next = self.right
        # point old tail's next to the new node
        oldTail.next = newNode
        # point the right's prev to point to the new node
        self.right.prev = newNode

    def appendleft(self, value: int) -> None:
        # for our implementation, the head will be the beginnign of the queue
        # create new node
        newNode = Node(value)
        # declare variable to the old head
        oldHead = self.left.next
        # new node's prev will point to left
        newNode.prev = self.left
        # new node's next will point to the old head
        newNode.next = oldHead
        # left's next will point to the new node
        self.left.next = newNode
        # old head's prev will point to the new node
        oldHead.prev = newNode
        

    def pop(self) -> int:
        # check if the doubly linked list is empty using our function
        if self.isEmpty():
            # if empty, return -1
            return -1
        # note: our end of the queue is the tail of the doubly linked list
        # start : left<->1<->2<->3<->right
        # end: left<->1<->2<->right
        # declare pointer to target node, aka the tail of the doubly linked list
        targetNode = self.right.prev
        # have the target node's prev, point to to target's next
        targetNode.prev.next = self.right
        # have right node's prev point to target node's prev
        self.right.prev = targetNode.prev
        # return the value of the target node 
        return targetNode.val
        

    def popleft(self) -> int:
        # check if the doubly linked list is empty using our function
        if self.isEmpty():
            # if empty, return -1
            return -1
        # note: our beginning of the queue is the head of the doubly linked list
        # declare pointer to target node, aka the head
        target = self.left.next
        # have target node's next, point to the target's prev, aka the left
        target.next.prev = self.left
        # left will point to target node's next
        self.left.next = target.next
        # return the value of the target node
        return target.val
        
