class DynamicArray:
    
    def __init__(self, capacity: int):
        # we need to declare and initalize the size for real numbers
        self.size = 0
        # declare and initalize the capacity for the datastructure
        self.capacity = capacity
        # declare and initalize the empty array with capacity
        # can we assume empty will be None?
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        # return the value of data's array at position i
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # set value of data's array at position i to value n
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # check if array is full, so check if size is equivalent to capacity
        if self.size == self.capacity:
            # if size is equal to capacity, resize
            self.resize()
        # push back the new value, n, to the end of the array, position size
        self.arr[self.size] = n
        # new number added, means the size increments
        self.size += 1

    def popback(self) -> int:
        # store last real number in the array
        lastValue = self.arr[self.size - 1]
        # override the last number with default value, None
        # do we want to use None? or 0 for default?
        self.arr[self.size - 1] = None
        # decrement the value size of the data structure
        self.size -= 1
        # return stored number, which was popped value
        return lastValue
 

    def resize(self) -> None:
        # create an array with new size, aka 2n (n represents current capacity)
        newArr = [None] * (2 * self.capacity)
        # iteratate from left to right of the current arr
        for i in range(0, self.capacity):
            # copy values of current array to new array
            # assign new arrays current value at index i to current array's value at index i
            newArr[i] = self.arr[i]
        
        # update the capacity
        self.capacity = 2 * self.capacity
        # assign the new array as the current array
        self.arr = newArr


    def getSize(self) -> int:
        # return the real number of elements
        return self.size
    
    def getCapacity(self) -> int:
        # return the capcity
        return self.capacity
