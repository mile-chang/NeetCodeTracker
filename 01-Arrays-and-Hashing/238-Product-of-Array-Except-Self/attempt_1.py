class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the output array with 1s
        res = [1] * len(nums)

        # Calculate the prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Calculate the postfix values and mutiply with the prefix to get result
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res