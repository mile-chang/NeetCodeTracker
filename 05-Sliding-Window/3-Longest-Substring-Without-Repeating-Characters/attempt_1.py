class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a set named window to store no duplicate characters.
        # Use sliding window to decrease time complexity to O(N)
        # Two-pointer ensuring O(N) time complexity by never re-scanning verified characters
        
        # 1. when to expand the window? (when ths s[i] in not in window)
        # 2. when to shrink the window? (when the s[i] in window)
        # 3. when to update the result? (when ths s[i] in not in window)

        window = set()
        # left pointer
        l = 0
        longest = 0

        # right pointer
        for r in range(len(s)):
            while s[r] in window:
                # when the s[r] in windown, we need shrink the window by remove the s[l] (FIFO)
                window.remove(s[l])
                # update the left point 
                l += 1
            window.add(s[r])
            length = r - l + 1
            longest = max(longest, length)
        return longest