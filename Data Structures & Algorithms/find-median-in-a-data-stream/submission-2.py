import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            biggestSmall = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, biggestSmall)
        
        if len(self.maxHeap) + 1 < len(self.minHeap):
            smallestBig = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * smallestBig)
        print("maxHeap: ", self.maxHeap)
        print("minHeap: ", self.minHeap)    

    def findMedian(self) -> float:
        # print("maxHeap: ", self.maxHeap)
        # print("minHeap: ", self.minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            return (-1 * self.maxHeap[0])
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        
        return (((-1 * self.maxHeap[0]) + self.minHeap[0]) / 2)
        