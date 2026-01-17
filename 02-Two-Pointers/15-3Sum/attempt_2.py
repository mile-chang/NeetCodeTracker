class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # In this case we can consist each indices than, the other two point, we can use two pointer to find its.
        # Notice that the solution set must not contain duplicate triplets.
        n = len(nums)
        nums.sort()
        res = []
        # Find each indices, left, right pointer, total value equal 0, then append to res[]
        # left, right = 1, n - 1
        for i in range(n):
            # it' already sorted, so if first value bigger than 0, result will be [].
            if nums[i] > 0:
                break
            # to avoid duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # to find another groups (total = 0)
                    left += 1
                    right -= 1
                    # to avoid duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res
        # -4, -1, -1, 0, 1, 2