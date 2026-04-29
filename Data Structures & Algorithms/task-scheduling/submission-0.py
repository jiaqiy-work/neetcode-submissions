class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)
        time = 0
        q = deque() # (-cnt, idleTime)

        while maxHeap or q:

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            time += 1
        return time


