class MinHeap:
    
    def __init__(self):
        self.heap = [0]        

    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap) - 1

        while (i // 2) > 0:
            if self.heap[i // 2] >= self.heap[i]:
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp
                i = i // 2
            else:
                break

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        elif len(self.heap) == 2:
            return self.heap.pop()
        
        top = self.heap[1]
        
        self.heap[1] = self.heap.pop()
        i = 1

        while (i * 2) < len(self.heap):
            if (i * 2) + 1 < len(self.heap) and self.heap[(i * 2) + 1] <= self.heap[i * 2] and self.heap[(i * 2) + 1] <= self.heap[i]:
                temp = self.heap[(i * 2) + 1]
                self.heap[(i * 2) + 1] = self.heap[i]
                self.heap[i] = temp
                i = (i * 2) + 1
            elif self.heap[i * 2] <= self.heap[i]:
                temp = self.heap[i * 2]
                self.heap[i * 2] = self.heap[i]
                self.heap[i] = temp
                i = i * 2
            else:
                break

        return top

    def top(self) -> int:
        return self.heap[1] if len(self.heap) >= 2 else -1

    def heapify(self, nums: List[int]) -> None:
        # [0, 1, 3, 4]
        if len(nums) == 0:
            self.heap = []
            return
        self.heap = nums
        nums.append(nums[0])
        self.heap[0] = 0

        cur = (len(nums) // 2 ) - 1

        while cur > 0:
            i = cur
            while (i * 2) < len(self.heap):
                if (i * 2) + 1 < len(self.heap) and self.heap[(i * 2) + 1] <= self.heap[i * 2] and self.heap[(i * 2) + 1] <= self.heap[i]:
                    temp = self.heap[(i * 2) + 1]
                    self.heap[(i * 2) + 1] = self.heap[i]
                    self.heap[i] = temp
                    i = (i * 2) + 1
                elif self.heap[i * 2] <= self.heap[i]:
                    temp = self.heap[i * 2]
                    self.heap[i * 2] = self.heap[i]
                    self.heap[i] = temp
                    i = i * 2
                else:
                    break
            cur -= 1



        