class Solution:
    def trap(self, height: List[int]) -> int:
        # how to calculate the each location of rain water?
        # each loaction i of rain water will be calculate by min(max_left, max_right) - height[i]
        
        # First we can traverse each current loaction's left and right to find max_left and max_right
        # but this will cause time complexity O(n2), how can we reduce the time complexity?

        # So, we use two pointer, we move the left and right toward to the middle, to calculate the max_left, max_right
        # it's will reduce time complexity to O(N), and we use constant to store max_left, max_right
        # space complexity will be O(1)

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        res = 0

        while left < right:
            # Find the bottleneck, then move the shorter side

            # when left is bottleneck
            if height[left] < height[right]:
                left += 1
                # update the max_left
                max_left = max(max_left, height[left])
                # Water trapped = boundary height - bar height
                # (if height[l] < max_left, it will cause hole, so the res will be increase)
                res += (max_left - height[left])
            # When right is bottleneck
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += (max_right - height[right])
        return res