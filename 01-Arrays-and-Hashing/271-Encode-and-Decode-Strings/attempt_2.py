class Solution:

    def encode(self, strs: List[str]) -> str:
        # we can use the number of each sting and '@' combine to one string.
        res = ''
        for s in strs:
            res += str(len(s)) + '@' + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        # we use two pointer to get the length of each string.
        # when we found '@' we split it.
        i = 0
        while i < len(s):
            j = i
            # we also need to avoid out of the range
            while s[j] != '@' and j < len(s):
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res