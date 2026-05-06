class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            if target-numbers[i] in numbers:
                idx = numbers.index(target-numbers[i])
                return [i+1, idx+1]
        return []