class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        n = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[n-1]:
                l = mid + 1
            else:
                r = mid
        
        def binary_search(nums, l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1
        
        result = binary_search(nums, l, n-1, target)
        if result == -1:
            result = binary_search(nums, 0,l, target)
        return result