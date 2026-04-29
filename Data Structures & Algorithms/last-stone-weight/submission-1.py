class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if -first > -second:
                new = -first + second
                heapq.heappush(stones, -new)
        
        if len(stones) == 1:
            return abs(stones[0])
        else:
            return 0
