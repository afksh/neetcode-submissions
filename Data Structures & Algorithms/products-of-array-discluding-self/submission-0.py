class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, num_a in enumerate(nums):
            product = 1
            for j, num_b in enumerate(nums):
                if i != j: product *= num_b 
            result.append(product)
        return result