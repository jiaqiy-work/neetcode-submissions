class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in nums:
            length = 1
            target = n + 1
            while target in numSet:
                length += 1
                target += 1
            res = max(res, length)
        return res