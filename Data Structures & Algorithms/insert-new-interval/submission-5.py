class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        res = []

        for i in range(len(intervals)):
            # newInterval ends before the current interval start
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # newInterval start after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # there is overlap between current interval and new interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
        
