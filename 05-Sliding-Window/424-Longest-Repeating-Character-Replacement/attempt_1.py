class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Note: this method not consider the consistent substring 
        # we calculate each charctor times
        # for c in s:
        #     count[c] = 1 + count.get(c, 0)
        
        # for c, freq in count.items():
        #     res = max(res, freq)
        # res += k 
        # return res

        # Use sliding window
        count = {}
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            # Expand: find the most freq elemnt
            char = s[r]
            count[char] = 1 + count.get(char, 0)
            max_freq = max(max_freq, count[char])
            window_length = r - l + 1

            # Shrink: if max_freq + k bigger than window_length, it's mean illegal
            if window_length - max_freq > k:
                count[s[l]] -= 1
                l += 1
            else:
                # When update the result (legal)
                res = max(res, window_length)
        return res