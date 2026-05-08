class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        l = 0
        r = len(intervals) - 1
        target = newInterval[0]

        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] < target:
                l = mid + 1
            else: 
                r = mid - 1
        intervals.insert(l, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res