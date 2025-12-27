class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # When we see sorted array and target, we can think of two pointer approach.
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            elif current_sum < target:
                left += 1  # Move left pointer to the right to increase sum
            else:
                right -= 1  # Move right pointer to the left to decrease sum
        return []  # Just in case there is no solution, though problem guarantees one