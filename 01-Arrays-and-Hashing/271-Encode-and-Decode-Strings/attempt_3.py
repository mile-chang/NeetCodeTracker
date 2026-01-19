class Solution:

    def encode(self, strs: List[str]) -> str:
        # we can use length of each string in strs to encode it
        # but the constraints say any possible charaters can in strs[i], it meam numbers also can in strs.
        # so we use '@' and length of each string in strs to encode it.
        # then, in decode, when we find '@', we also check before '@' is numbers or not, is number, than we split it by numbers of lengh.
        encodestr = ""
        for s in strs:
            strings = str(len(s)) + '@' + s
            encodestr += strings
        return encodestr

    def decode(self, s: str) -> List[str]:
        # we input the encodesdr
        # first, we need to find '@'
        decodestrings = []
        # time complexity o(m+n)
        # when we find '@',then how to find before '@' numbers of length
        # we use while loop instead of for loop to skip the strings already seen.
        i = 0
        while i < len(s):
            # we need two pointer hear, i is the original, j is to find the length before '@' 
            j = i
            # to calculate before '@' strings length.
            while s[j] != '@':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            decodestrings.append(s[start:end])
            i = end
        return decodestrings