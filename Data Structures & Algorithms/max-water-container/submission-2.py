class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0
        
        while l < r:
            ans = max(ans, (r-l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return ans