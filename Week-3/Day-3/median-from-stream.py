import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        self.md = -10 ** 5

    def addNum(self, n: int) -> None:
        if n > self.md:
            heapq.heappush(self.minHeap, n)
        else:
            heapq.heappush(self.maxHeap, -1 * n)
            
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
            else:
                heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
                
        if len(self.maxHeap) == len(self.minHeap):
           self.md = (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0
        elif len(self.maxHeap) > len(self.minHeap):
            self.md = -1 * self.maxHeap[0]
        else:
            self.md = self.minHeap[0]
            
    def findMedian(self) -> float:
        return self.md


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()