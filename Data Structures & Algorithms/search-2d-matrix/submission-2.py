class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            idx = (l + r) // 2
            num = matrix[idx//n][idx%n]
            if num == target:
                return True
            elif num < target:
                l = idx + 1
            else:
                r = idx - 1
        return False