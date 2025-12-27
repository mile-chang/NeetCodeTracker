class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # First: when we see group or duplicate question, maybe we can use the hash map.
        from collections import defaultdict
        res = defaultdict(list) # avoid key error

        for s in strs:
            # Second: we use the character count as the key.
            count = [0] * 26
            for c in s:
                # locate the character position of the string
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # use tuple to convert list to hashable key
        return list(res.values())