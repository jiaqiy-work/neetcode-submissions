class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []

        for i in range(k):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(max_heap, (-distance, i))

        for i in range(k,len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            top_distance = max_heap[0][0]
            if distance < -top_distance:
                heapq.heappushpop(max_heap, (-distance, i))
        
        for _ in range(k):
            idx = heapq.heappop(max_heap)
            result.append(points[idx[1]])

        return result

   