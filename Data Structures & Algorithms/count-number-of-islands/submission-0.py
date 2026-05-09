class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        res = 0

        def dfs(i, j):

            if i not in range(m) or j not in range(n) or grid[i][j] == "0" or (i, j) in visit:
                return
            
            visit.add((i, j))

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visit:
                    res += 1
                    dfs(i, j)
        return res