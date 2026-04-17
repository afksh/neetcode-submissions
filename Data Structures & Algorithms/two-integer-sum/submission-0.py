class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            target_delta = target - num
            if target_delta in indices:
                return [indices[target_delta], i]
            indices[num] = i