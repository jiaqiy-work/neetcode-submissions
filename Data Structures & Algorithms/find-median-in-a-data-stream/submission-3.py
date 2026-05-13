class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.size = 0
        

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -1 * num)

        len_max_heap = len(self.max_heap)
        len_min_heap = len(self.min_heap)

        if (len_max_heap - len_min_heap) > 1:
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1 * num)

        if (len_min_heap - len_max_heap) > 1:
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * num)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap): 
            return -1 * self.max_heap[0]
        return (self.min_heap[0] + -1*self.max_heap[0]) / 2.0
        