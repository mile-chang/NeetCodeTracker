class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set of numbers for O(1) lookups
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Only start counting if 'num' is the start of a sequence
            if num - 1 not in numSet:
                length = 1
                # Count the length of the sequence
                while num + 1 in numSet:
                    length += 1
                longest = max(longest, length)
        return longest