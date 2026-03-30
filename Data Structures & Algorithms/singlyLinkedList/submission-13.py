class Node:
    def __init__(self, value=-1):
        self.val = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        # to remove edge cases, we initalize a dummy node that will be 
        # to the left of the head
        # declare dummyNode
        self.left = Node()
        # declare tail to none
        self.tail = None

    
    def get(self, index: int) -> int:
        # declare and initalize counter to 0
        counter = 0
        # iterate through list starting at head until counter hits index or current pointer hits none
        # head will be represented by dummyNode
        head = self.left.next
        while head and counter != index:
            head = head.next
            counter += 1

        # check if pointer not to none and counter is equal to index
        if head and counter == index:
            # if true -> return current value at pointer
            return head.val

        # return -1
        return -1
        

    def insertHead(self, val: int) -> None:
        # declare and initalize new node with value of val
        newNode = Node(val)
        # set new node's next to the current head
        newNode.next = self.left.next
        # insert newNode to the right of left node
        self.left.next = newNode

        # if tail is not set, set it to head
        if self.tail == None:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        # declare and initalize new Node w/ value as val
        newNode = Node(val)
        # check if tail is None -> set new new Node as head and tail
        if self.tail == None:
            self.left.next = newNode
            self.tail = newNode
        else:
            #else
            # set tail's next to newNode
            self.tail.next = newNode
            # set tail as newNode
            self.tail = newNode
        

    def remove(self, index: int) -> bool:
        # left -> 1 -> 2 -> None

        # decalre and initialize dummyNode to left node
        node = self.left
        # declare and intialize counter
        counter = 0
        # while dummyNode is not none and counter is < index
        while node and counter < index:
            #   move dummyNode over one position
            node = node.next
            #   increment counter
            counter += 1
        
        # if dummyNode is not none and dummyNode's next is not none and index == counter
        if node and node.next and counter == index:
            # check if the node to be removed is the tail
            if node.next == self.tail:
                # if tail -> set current node as the new tail
                self.tail = node
            # have dummyNode node's next be dummyNode's next next
            node.next = node.next.next
            # return True
            return True

        # return False
        return False
        

    def getValues(self) -> List[int]:
        # declare and initalize list
        values = []
        # declare dummy point to head
        currNode = self.left.next
        # iterate through the linked list starting at head 
        while currNode:
            # add the current node's value to the list
            values.append(currNode.val)
            # move currNode over one position
            currNode = currNode.next

        # return list
        return values
        
