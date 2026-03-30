class DynamicArray:
    
    def __init__(self, capacity: int):
        # set the size to 0
        self.size = 0
        # create the allocation for the dynamic array using list to the capacity
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # get the array value from the list at given index
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        # set the array value at index n
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        # check if array is full -> if true -> resize array called
        if self.size == len(self.arr):
            self.resize()

        # set array value to n at index size (use set())
        self.arr[self.size] = n
        # increase size
        self.size = self.size + 1

    def popback(self) -> int:
        # store the value from array at index (size - 1)
        poppedVal = self.arr[self.size - 1]
        # set value at index (size -1) to 0
        self.arr[self.size - 1] = 0
        # decrement size
        self.size = self.size - 1
        # return popped value
        return poppedVal

    def resize(self) -> None:
        # create an array with double the capacity with 0s
        newArr = [0] * 2 * len(self.arr)
        # iterate through array and paste it into the new array
        for i in range(0, len(self.arr)):
            newArr[i] = self.arr[i]

        # set new array as the array for the datastructure
        self.arr = newArr
        


    def getSize(self) -> int:
        # return size
        return self.size
    
    def getCapacity(self) -> int:
        # return capcity
        return len(self.arr)
