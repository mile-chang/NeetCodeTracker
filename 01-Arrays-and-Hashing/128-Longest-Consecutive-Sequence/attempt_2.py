class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                # Count the length of the sequence, n + 1, n + 2, ...
                while n + length in numSet:
                    length += 1
                res = max(res, length)
        return res