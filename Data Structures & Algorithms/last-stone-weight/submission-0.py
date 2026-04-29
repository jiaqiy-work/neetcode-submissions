class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, -s)
        
        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            if first == second:
                continue
            if -first > -second:
                new = -first + second
                heapq.heappush(max_heap, -new)
        
        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0
