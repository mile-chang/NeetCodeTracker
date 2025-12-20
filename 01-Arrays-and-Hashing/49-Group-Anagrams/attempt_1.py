class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We use a hashmap to group anagrams
        # Defaultdict to automatically handle missing keys
        result = defaultdict(list)

        for s in strs:
            # Calculate the character count for each string
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Use the character count tuple as a key
            result[tuple(count)].appends(s)
        # Use list to convert the values to a list of lists
        return list(result.values())