class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first: need to find the start of the cosecutive sequence
        # how to find the start -> when the charator - 1 not exist, it's mean this charctor is the start.
        # second find the longest -> while the start + 1 is exist, lenght += 1
        # final longest = max(length, longest)
        # time complexity = O(N), space complexity = O(N)
        # Notes: List using the in operator takes O(n) time. By converting the list to a set, lookups become O(1).

        longest = 0
        # converting the list to a set
        num_set = set(nums)

        for n in num_set:
            # find the start of sequence
            if n - 1 not in num_set:
                length = 1
                # Note: n + 1 will cause loop, need use n + length
                while n + length in num_set:
                    length += 1
                longest = max(length, longest)
        return longest