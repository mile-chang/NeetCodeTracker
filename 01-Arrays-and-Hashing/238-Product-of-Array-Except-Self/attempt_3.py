class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # without division, we can use prefix and postfix products
        # we can create two arrays or we can do it in one pass with O(1) space
        n = len(nums)
        res = [1] * n

        # Step1: calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        # Step2: calculate postfix products and multiply with prefix products
        postfix = 1
        # we need to go from the end to the start (until index 0)
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res