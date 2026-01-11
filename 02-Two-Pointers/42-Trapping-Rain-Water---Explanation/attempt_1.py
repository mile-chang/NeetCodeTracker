class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0

        while l < r:
            # Determine which side is bottleneck, then move that pointer inward
            # Each index of rain amount = min(max_left, max_right) - height[i]
            if max_left < max_right:
                l += 1
                # Update max_left and calculate trapped water at index l
                max_left = max(max_left, height[l])
                res += (max_left - height[l])
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += (max_right - height[r])
        return res