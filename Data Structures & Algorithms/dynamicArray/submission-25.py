class DynamicArray:
    
    def __init__(self, capacity: int):
        # initiaze the array with the appropriate capacity
        self.arr = [None] * capacity
        # declare and initialize variable to see capacity
        # self.capacity = capacity
        # declare and intialize variable to know real number amount
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        # retrieve array value's value at i, and return it
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # set value n to array[i]
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # check if array is full, reisize if so
        if self.size == self.capacity:
            self.resize()
        # we set the element n to the end of the array which will be at index size
        self.arr[self.size] = n
        # increment the value storing size
        self.size = self.size + 1

    def popback(self) -> int:
        # get value at last real value
        realVal = self.arr[self.size - 1]
        # set value of arr[last element index] to default/0
        self.arr[self.size - 1] = None
        # decrement the array's size property
        self.size = self.size - 1
        return realVal

    def resize(self) -> None:
        # can we assume we copy the previous elements as well, not just create a new size with double the capacity?
        # create variable and initalize it to an array with 2 * length of curren array
        arrLen = self.capacity
        newArr = [None] * (2 * arrLen)
        # iterate through the current array from left to right
        for i in range(0, arrLen):
            # paste the current array elemet at current index to the new array at current index
            newArr[i] = self.arr[i]
        # set the new array as the current array
        self.capacity = len(newArr)
        self.arr = newArr

    def getSize(self) -> int:
        # return the actual value amount
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
