class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # constraint: without using the divsion operation
        # nums[i] can be 0 or minus.

        # we can use prefix and postfix to solve this problem
        # nums[i] can be dived sum of prefix * sum of postfix
        res = [1] * len(nums)

        # Calculate each nums[i]'s prefix (from left to right)
        prefix = 1 # To keep the result unchanged
        for i in range(len(nums)):
            res[i] = prefix
            # update the prefix
            prefix *= nums[i]
        
        # Calculate each nums[i]'s postfix and the result (from right to left)
        postfix = 1
        for j in range(len(nums) - 1, -1, -1): # (include, not include, -1)
            res[j] *= postfix
            postfix *= nums[j]
        return res