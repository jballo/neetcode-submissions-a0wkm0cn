class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size = self.size + 1

    def popback(self) -> int:
        temp = self.arr[self.size-1]
        self.size = self.size - 1
        return temp
 

    def resize(self) -> None:
        newCapacity = 2 * len(self.arr)
        newArr = [0] * newCapacity
        for i in range(0, len(self.arr)):
            newArr[i] = self.arr[i]
        self.capacity = newCapacity
        self.arr = newArr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
