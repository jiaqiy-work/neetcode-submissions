class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        area = 0

        def bfs(i, j):
            q = collections.deque()
            visit.add((i, j))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q.append((i, j))
            a = 1
            while q:
                row, col = q.popleft()

                for r, c in directions:
                    nr = row + r
                    nc = col + c
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == 1 and (nr, nc) not in visit:
                        a += 1
                        visit.add((nr, nc))
                        q.append((nr, nc))
            return a


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    area = max(area, bfs(i, j))

        return area