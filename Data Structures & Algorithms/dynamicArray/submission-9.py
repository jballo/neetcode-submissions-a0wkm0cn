class DynamicArray:
    
    def __init__(self, capacity: int):
        # what do we consider empty
        self.arr = [None] * capacity
        self.cap = capacity
        self.size = 0

    def get(self, i: int) -> int:
        # return the value at arr's ith index
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # by valid index, there is a value in the ith index?
        # change the value at the ith index to self's arr
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # is there a certain order in which pusback needs to be done?
        # if size == capacity-1
        if self.size == (self.cap):
            #   call resiz
            self.resize()
        
        # set last index in array to the value n, and then resize 
        # last index is size?
        # set arr[size] to n value
        self.arr[self.size] = n
        # increment size
        self.size += 1
        

    def popback(self) -> int:
        # we return the value of arr at index [size -1]?
        # store arr[size-1]
        lastVal = self.arr[self.size - 1]
        # set arr[size-1] to None
        self.arr[self.size - 1] = None
        # decrement size
        self.size -= 1
        # return the stored value
        return lastVal

    def resize(self) -> None:
        # can i assume I can allocate more space for resize?
        # create a new array that is double the capacity that is empty
        newArr = [None] * (self.cap * 2)
        self.cap *= 2
        # copy all the values in arr into the new array
        for i in range(0, self.size):
            newArr[i] = self.arr[i]
        # set arr to the new arr
        self.arr = newArr

    def getSize(self) -> int:
        # do we want this to be done in O(1) or O(N) for time        
        # return the value of size
        return self.size

    def getCapacity(self) -> int:
        # do we want this to be done in O(1) or O(N) for time
        # return capacity value
        return self.cap
