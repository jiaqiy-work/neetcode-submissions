class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        preMap = {i: [] for i in range(numCourses)}
        visit, cycle = set(), set()
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output