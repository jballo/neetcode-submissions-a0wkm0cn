class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.perculateUp(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()

        top = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.perculateDown(1)
        return top

    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        for i in range(len(self.heap) // 2, 0, -1):
            self.perculateDown(i)

    def perculateUp(self, i):
        parent = i // 2
        while i > 1 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = i // 2

    def perculateDown(self, i):
        child = i * 2
        while child < len(self.heap):
            if (child + 1) < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child = child + 1

            if self.heap[i] <= self.heap[child]:
                break
            
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child
            child = i * 2
        