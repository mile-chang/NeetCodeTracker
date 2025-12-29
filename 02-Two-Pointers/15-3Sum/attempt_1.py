class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # we sort the array to make two pointer approach possible
        nums.sort()
        
        # Use enumerate to get both index and value
        for i, n in enumerate(nums):
            # Skip duplicate values for the first number
            if i > 0 and n == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = n + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # We dont need to skip duplicates for the third number here
                    # because the right pointer is moving leftwards