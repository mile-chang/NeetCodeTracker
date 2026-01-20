class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we can use two pointer, init mostWater = 0
        # we need to find the highest left bar and right bar.
        # container of the water = length * min(left, right)

        left, right = 0, len(heights) - 1
        mostWater = 0

        while left < right:
            length = right - left
            water = length * min(heights[left], heights[right])
            mostWater = max(water, mostWater)
            # the minimize is left, so if we need to find the more bigger container of the water, we need to move left
            if heights[left] < heights[right]:
                left += 1
            # heights[left] >= heights[right] also move right, that can get the bigger water
            else:
                right -= 1
        return mostWater