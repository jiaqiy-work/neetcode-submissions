class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hashmap = {} # index: interval_length
        res = [float('inf')] * len(queries)
        for i in range(len(intervals)):
            hashmap[i] = intervals[i][1] - intervals[i][0] + 1
        
        for i in range(len(queries)):
            for j in range(len(intervals)):
                interval = intervals[j]
                if interval[0] <= queries[i] and queries[i] <= interval[1]:
                    res[i] = min(res[i], hashmap[j])
            if res[i] == float('inf'):
                res[i] = -1
        return res
        
