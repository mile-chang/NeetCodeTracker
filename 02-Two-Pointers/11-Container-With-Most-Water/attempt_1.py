class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            # When heights are equal or heights[right] is smaller, we move the right pointer
            else:
                right -= 1