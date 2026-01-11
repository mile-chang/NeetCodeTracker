class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        
        for s in strs:
            count = [0] * 26  # There are 26 letters in the English alphabet
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Use the tuple of counts as the key for the same count strings.
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())