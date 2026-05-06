class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
       
        prefix_prod = [0] * n
        suffix_prod = [0] * n
        result = [0] * n

        prefix_prod[0] = suffix_prod[n-1] = 1
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix_prod[i] = suffix_prod[i + 1] * nums[i + 1]
        for i in range(n):
            result[i] = prefix_prod[i] * suffix_prod[i]
        return result

